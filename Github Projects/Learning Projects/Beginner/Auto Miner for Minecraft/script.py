import pyautogui as pt
from pyfiglet import Figlet
from time import sleep
import sys

# === MENU === 
def ascii_title():
    f = Figlet(font='doom')
    return f.renderText("Mine-Script")

def menu():
    return f"""
{ascii_title()}
                Welcome User! 
               By: Evan William
"""

def dot_generate(word):
    for i in range(4):
        dots = "." * i
        print(f"\r{word}{dots}", end='', flush=True)
        sleep(0.5)

# === CONFIG ===  # CHANGE THESE PATHS ACCORDINGLY
LAVA_IMAGE = r"D:\College\Programming Files\Codes\Projects\Github Projects\Learning Projects\Beginner\Auto Miner for Minecraft\images\lava.png"
START_IMAGE = r"D:\College\Programming Files\Codes\Projects\Github Projects\Learning Projects\Beginner\Auto Miner for Minecraft\images\start_game.png"

# === UTILITIES ===
def safe_locate(*image_paths, confidence=0.8):
    for image_path in image_paths:
        try:
            position = pt.locateCenterOnScreen(image_path, confidence=confidence)
            if position:
                return position
        except Exception as e:
            print(f"Debug: Error locating {image_path}: {e}")
            pass
    return None

def navigate_to_img(image, clicks=1, off_x=0, off_y=0, confidence=0.8):
    pos = safe_locate(image, confidence=confidence)
    if pos is not None:
        pt.moveTo(pos, duration=0.2)
        pt.moveRel(off_x, off_y, duration=0.1)
        pt.click(clicks=clicks, interval=0.2)
        return True
    else:
        print(f"❌ Start button not found!")
        return False

def move_character(key_press, duration, action='walking'):
    pt.keyDown(key_press)

    if action == 'walking':
        dot_generate("🚶 Walking")
    elif action == 'attack':
        pt.keyDown('x')
        dot_generate("⛏️  Mining")

    sleep(duration)
    pt.keyUp('x')
    pt.keyUp(key_press)

def locate_lava():
    print("🌋 Checking for lava...")
    # Fixed: Only use LAVA_IMAGE and increased confidence
    lava_pos = safe_locate(LAVA_IMAGE, confidence=0.8)
    if lava_pos:
        print(f"🔥 Lava detected at position: {lava_pos}")
        move_character('s', 3)
        dot_generate("💀 Exiting Script")
        sys.exit(0)
    else:
        print("✅ No lava found!")
        return False

# === MAIN BOT ===
def start_bot():
    dot_generate("🎮 Trying to start the game")
    if not navigate_to_img(START_IMAGE, clicks=3):
        dot_generate("❌ Failed to find start button. Exiting bot")
        return

    dot_generate("✅ Game started! Beginning mining")
    print("\n")
    cycles = BOT_DURATION

    while cycles > 0:
        if not locate_lava():
            move_character('w', 2, action='attack')
        else:
            break

        cycles -= 1
        print(f"\n⏳ Time remaining: {cycles} cycle(s) left\n")
        sleep(1)

    print("🏁 Mining session completed!")

# === ENTRY POINT ===
if __name__ == "__main__":
    print(menu())
    duration_input = int(input("Input Bot's Duration: "))
    BOT_DURATION = duration_input

    for each in range(5, 0, -1):
        print(f"\rScript starting in {each}...", end='', flush=True)
        sleep(1)

    print("\n🚀 Starting now!")
    start_bot()