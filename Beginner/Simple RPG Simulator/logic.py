import inquirer
import time
from menus import menu2, clear_screen
from adventure import startadventure
from shop import startshop
from stats import seestats, reset_health

def begin():
    reset_health()
    print(menu2())
    while True:
        choice = [
            inquirer.List(
                "Action",
                message="Choose an action!",
                choices=["Adventure", "Shop", "Stats", "Exit"]
            )
        ]
        answer = inquirer.prompt(choice)

        if answer["Action"] == "Adventure":
            clear_screen()
            startadventure()
            break
        elif answer["Action"] == "Shop":
            clear_screen()
            startshop()
            break
        elif answer["Action"] == "Stats":
            clear_screen()
            seestats()
            break
        else:
            print("Exiting game...")
            time.sleep(1)
            break

def startgame():
    clear_screen()
    print("Game Starting.")
    time.sleep(1)
    clear_screen()
    print("Game Starting..")
    time.sleep(1)
    clear_screen()
    print("Game Starting...")
    time.sleep(1)
    clear_screen()
    print("Game Loaded!")
    begin()
