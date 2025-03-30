from menus import menu1, clear_screen
from authentication import startregister, startlogin
import inquirer
import time

def main():
    while True:
        clear_screen()
        print(menu1())
        questions = [
            inquirer.List(
                "choice",
                message="Choose an option",
                choices=["Register", "Login", "Exit"]
            )
        ]
        answer = inquirer.prompt(questions)
        if answer["choice"] == "Register":
            startregister()
            break
        elif answer["choice"] == "Login":
            startlogin()
            break
        else:
            print("Exiting game...")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()
