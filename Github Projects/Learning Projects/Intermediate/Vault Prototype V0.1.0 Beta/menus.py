from pyfiglet import Figlet
import platform
import subprocess

# 1. Clear Screen
def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

# 2. Menu Set & Menu Print 
def maintitle():
    f = Figlet(font='slant')
    return f.renderText("Vault")

def authtitle():
    f = Figlet(font='slant')
    return f.renderText("Auth")

def logintitle():
    f = Figlet(font='slant')
    return f.renderText("Credential")

def menu():
    return f"""
{maintitle()}
                Welcome User! 
               By: Evan William
"""

def auth_menu():
    return f"""
{authtitle()}
                Welcome User!
    Please input your database information:
"""

def cred_menu():
    return f"""
{logintitle()}
                Welcome User!
    Please input your credential information:
"""