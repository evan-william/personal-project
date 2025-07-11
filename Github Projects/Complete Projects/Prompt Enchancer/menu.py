from pyfiglet import Figlet
import platform
import subprocess

def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def ascii_title():
    f = Figlet(font='slant')
    return f.renderText("Prompt+")

def ascii_title2():
    f = Figlet(font='slant')
    return f.renderText("API-KEY")

def menu():
    return f"""
{ascii_title()}
                Welcome User! 
               By: Evan William
"""

def auth_menu():
    return f"""
{ascii_title2()}
                Welcome User!
    Please input your gemini api key:
"""