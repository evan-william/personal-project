from pyfiglet import Figlet
import random
import sys
import platform
import subprocess
import time
import inquirer

class Compute():
    def __init__(self):
        self.number = 0
        self.wanted = 1

    def generate(self):
        try:
            wanted = int(input("Enter How Long: "))
            printing = pow(10,wanted)

            wants = random.randint(1,printing)

            print(wants)
        except ValueError:
            print("Not a valid input!")
            sys.exit(0)

    def clear_screen(self):
        if platform.system() == "Windows":
            subprocess.run("cls", shell=True)
        else:
            subprocess.run("clear", shell=True)

    def ascii_title1(self):
        f = Figlet(font='slant')
        return f.renderText("NumGen")

    def menu1(self):
        return f"""
{self.ascii_title1()}
                     Welcome User! 
                    By: Evan William
"""

def main():
    compute = Compute()
    print(compute.menu1())
    compute.generate()


if __name__ == "__main__":
    main()
