import subprocess
import time
import pyautogui

# Path to Riot Client executable (Adjust Please!)
VALORANT_PATH = # Fill This

"""
For example:
r"D:\Games\VALORANT\Riot Games\Riot Client\RiotClientServices.exe"
"""

# Fill Both
USERNAME = ""
PASSWORD = ""

def open_valorant():
    subprocess.Popen(VALORANT_PATH)
    time.sleep(10)  

def login():
    time.sleep(5)

    pyautogui.click(900, 500)  
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(USERNAME)
    time.sleep(0.5)

    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(USERNAME)
    time.sleep(0.5)

    pyautogui.press("tab")
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(PASSWORD)
    time.sleep(0.5)

    pyautogui.press("enter")
    time.sleep(2)

if __name__ == "__main__":
    open_valorant()
    time.sleep(10)
    login()
