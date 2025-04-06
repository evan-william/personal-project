import os
import time
import winsound
import pyautogui
import random

def main():
    messages = ["HAHAHAHA", "Error 404: Why so stupid?!", "Have fun closing these!", "Guess what? More pop-ups!"]
    
    while True:
        os.system("notepad")
        winsound.Beep(random.randint(500, 2000), random.randint(300, 800))

        x, y = pyautogui.size()
        pyautogui.moveTo(random.randint(0, x), random.randint(0, y), duration=0.5)

        pyautogui.alert(random.choice(messages), "PLEASE RESTART YOUR DEVICE")

        if random.choice([True, False]):
            os.system("calc")  
        else:
            os.system("mspaint")  

        time.sleep(2) 

main()
