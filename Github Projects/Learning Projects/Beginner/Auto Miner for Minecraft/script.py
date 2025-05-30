import pyautogui as pt
from pyfiglet import Figlet
from time import sleep


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

# === CONFIG === # CHANGE THIS PATH ACCORDINGLY 
LAVA_IMAGE = r"D:\College\Programming Files\Codes\Projects\Github Projects\Learning Projects\Beginner\Auto Miner for Minecraft\images\lava.png"
START_IMAGE = r"D:\College\Programming Files\Codes\Projects\Github Projects\Learning Projects\Beginner\Auto Miner for Minecraft\images\start_game.png"


# === UTILITIES ===
def safe_locate(image_path, confidence=0.8):
    try:
        position = pt.locateCenterOnScreen(image_path, confidence=confidence)
        return position
    except pt.ImageNotFoundException:
        return None


def navigate_to_img(image, clicks=1, off_x=0, off_y=0, confidence=0.8):
    print(f"Trying to locate: {image}")
    pos = safe_locate(image, confidence)
    if pos is not None:
        pt.moveTo(pos, duration=0.2)
        pt.moveRel(off_x, off_y, duration=0.1)
        pt.click(clicks=clicks, interval=0.2)
        print(f"Clicked on: {image}")
        return True
    else:
        print(f"{image} not found!")
        return False


def move_character(key_press, duration, action='walking'):
    pt.keyDown(key_press)

    if action == 'walking':
        print("Walking...")
    elif action == 'attack':
        pt.keyDown('x')
        print("Mining...")

    sleep(duration)
    pt.keyUp('x')
    pt.keyUp(key_press)


def locate_lava():
    print("Checking for lava...")
    lava_pos = safe_locate(LAVA_IMAGE, confidence=0.8)
    if lava_pos:
        print("🔥 Lava detected! Retreating!")
        move_character('s', 2)
        return True
    else:
        print("No lava found.")
        return False


# === MAIN BOT ===

def start_bot():
    print("\nTrying to start the game...")
    if not navigate_to_img(START_IMAGE, clicks=3):
        print("❌ Failed to find start button. Exiting bot.")
        return

    print("✅ Game started! Starting bot operations...\n")
    cycles = BOT_DURATION

    while cycles > 0:
        if not locate_lava():
            move_character('w', 2, action='attack')
        else:
            break

        cycles -= 1
        print(f"⏳ Time remaining: {cycles} cycle(s) left\n")
        sleep(1)


# === ENTRY POINT ===
if __name__ == "__main__":
    print(menu())
    duration_input = int(input("Input Bot's Duration: "))
    BOT_DURATION = duration_input  # How many cycles the bot runs

    for each in range(5, 0, -1):
        print(f"\rScript starting in {each}...", end='', flush=True)
        sleep(1)

    print("\n🚀 Starting now!")
    start_bot()
