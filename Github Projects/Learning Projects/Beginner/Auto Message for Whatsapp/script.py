import pyautogui as pt
from pyfiglet import Figlet
from time import sleep
import sys
import datetime

# === MENU === 
def ascii_title():
    f = Figlet(font='doom')
    return f.renderText("WA-Script")

def menu():
    return f"""
{ascii_title()}
            Auto WhatsApp Messenger! 
               By: Evan William
"""

def dot_generate(word):
    for i in range(4):
        dots = "." * i
        print(f"\r{word}{dots}", end='', flush=True)
        sleep(0.5)

# === CONFIG ===  # CHANGE THESE PATHS ACCORDINGLY
WHATSAPP_ICON = r"D:\College\Programming Files\Codes\Projects\Github Projects\Learning Projects\Beginner\Auto Message for Whatsapp\images\whatsapp.png"  # WhatsApp desktop icon
CONTACT_IMAGE = r"D:\College\Programming Files\Codes\Projects\Github Projects\Learning Projects\Beginner\Auto Message for Whatsapp\images\contact_target.png"        # Target contact image

# === UTILITIES ===
def safe_locate(*image_paths, confidence=0.8):
    for image_path in image_paths:
        try:
            position = pt.locateCenterOnScreen(image_path, confidence=confidence)
            if position:
                return position
        except Exception as e:
            print(f" Debug: Error locating image: {e}")
            pass
    return None

def navigate_to_img(image, clicks=1, off_x=0, off_y=0, confidence=0.8, wait_time=2):
    pos = safe_locate(image, confidence=confidence)
    if pos is not None:
        pt.moveTo(pos, duration=0.5)
        pt.moveRel(off_x, off_y, duration=0.1)
        pt.click(clicks=clicks, interval=0.3)
        sleep(wait_time)  
        return True
    else:
        return False

def open_whatsapp():
    print("📱 Opening WhatsApp...")
    dot_generate("🔍 Looking for WhatsApp icon")
    
    if navigate_to_img(WHATSAPP_ICON, clicks=1, confidence=0.8, wait_time=5):
        print("✅ WhatsApp opened successfully!")
        return True
    else:
        print("❌ WhatsApp icon not found on desktop!")
        return False

def select_contact():
    dot_generate("👤 Looking for contact")
    dot_generate("🔍 Searching for contact")
    
    sleep(4)
    
    if navigate_to_img(CONTACT_IMAGE, clicks=1, confidence=0.8, wait_time=2):
        print("✅ Contact found and selected!")
        return True
    else:
        print("\n❌ Contact not found!")
        return False

def send_message(message):
    print(f"💬 Sending message: '{message}'")
    
    sleep(2)
    
    # Type the message
    pt.typewrite(message, interval=0.05)
    sleep(0.5)
    
    # Press Enter to send
    pt.press('enter')
    print("✅ Message sent!")

def calculate_wait_time(target_time):
    now = datetime.datetime.now()
    target = datetime.datetime.strptime(target_time, "%H:%M").replace(
        year=now.year, month=now.month, day=now.day
    )
    
    # If target time is earlier than now, assume it's for tomorrow
    if target < now:
        target += datetime.timedelta(days=1)
    
    wait_seconds = (target - now).total_seconds()
    return wait_seconds

def format_time_remaining(seconds):
    """Format seconds into a readable time string"""
    if seconds <= 0:
        return "00:00:00"
    
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def wait_until_time(target_time):
    """Wait until target time with real-time countdown display"""
    initial_wait = calculate_wait_time(target_time)
    
    if initial_wait <= 0:
        print("⏰ Target time has already passed or is now. Sending immediately...")
        return
    
    print(f"⏰ Waiting until {target_time}...")
    
    # Real-time countdown loop
    while True:
        current_wait = calculate_wait_time(target_time)
        
        if current_wait <= 0:
            print(f"\r🚀 Time reached! Sending now...                    ")
            break
        
        time_str = format_time_remaining(current_wait)
        
        # Different messages based on time remaining
        if current_wait <= 10:
            print(f"\r⏳ Sending in {int(current_wait)} seconds... ", end='', flush=True)
        elif current_wait <= 60:
            print(f"\r⏳ Time remaining: {time_str} (Less than a minute!) ", end='', flush=True)
        elif current_wait <= 300:  # 5 minutes
            print(f"\r⏰ Time remaining: {time_str} (Almost time!) ", end='', flush=True)
        else:
            print(f"\r⏰ Time remaining: {time_str} ", end='', flush=True)
        
        # Update every second
        sleep(1)
    
    print()  # New line after countdown

def start_messaging_bot(message, send_time, repeat_count):
    dot_generate("🚀 Starting WhatsApp Auto Messenger")
    
    # Step 1: Open WhatsApp
    if not open_whatsapp():
        print("❌ Failed to open WhatsApp. Exiting...")
        return
    
    # Step 2: Select contact
    if not select_contact():
        print("❌ Failed to find contact. Exiting...")
        return
    
    # Step 3: Wait until target time ONCE (before sending any messages)
    if send_time and send_time != "now":
        wait_until_time(send_time)
    
    # Step 4: Send all messages after the wait time
    print(f"\n🚀 Starting to send {repeat_count} message(s)...")
    
    for i in range(repeat_count):
        print(f"\n📨 Sending message {i+1}/{repeat_count}")
        
        # Send the message
        try:
            send_message(message)
            print(f"✅ Message {i+1}/{repeat_count} sent successfully!")
            
            # Wait 2 seconds between messages if sending multiple
            if i < repeat_count - 1:
                print("⏸️  Waiting 2 seconds before next message...")
                sleep(2)
                
        except Exception as e:
            print(f"❌ Error sending message {i+1}: {e}")
            break
    
    print(f"\n🎉 All messages sent! Total: {repeat_count}")

def validate_time_format(time_str):
    if time_str.lower() == "now":
        return True
    try:
        datetime.datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

# === STARTING POINT ===
if __name__ == "__main__":
    print(menu())
    
    # Get user inputs
    print("📝 Please provide the following information:\n")
    
    # Message input
    message = input("💬 Message: ").strip()
    if not message:
        print("❌ Message cannot be empty!")
        sys.exit(1)
    
    # Time input
    while True:
        send_time = input("⏰ Time (HH:MM or 'now'): ").strip()
        if validate_time_format(send_time):
            if send_time.lower() == "now":
                send_time = None
            break
        else:
            print("❌ Invalid time format! Use HH:MM (24-hour) or 'now'")
    
    # Repeat count input
    while True:
        try:
            repeat_count = int(input("🔄 How many times: ").strip())
            if repeat_count > 0:
                break
            else:
                print("❌ Number must be greater than 0!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Confirmation to USER
    print(f"\n📋 Summary:")
    print(f"   Message: '{message}'")
    print(f"   Time: {'Immediately' if not send_time else send_time}")
    print(f"   Repeat: {repeat_count} time(s)")
    
    confirm = input("\n✅ Continue? (y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ Operation cancelled.")
        sys.exit(0)
    
    # Countdown before starting!
    print()
    dot_generate("🔄 Starting")
    sleep(1)

    start_messaging_bot(message, send_time, repeat_count)
