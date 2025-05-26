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
    return f.renderText("Quiz App")

def ascii_title2():
    f = Figlet(font='slant')
    return f.renderText("Credential")

def ascii_title3():
    f = Figlet(font ='slant') 
    return f.renderText("DB Auth")

def ascii_title4():
    f = Figlet(font='slant')
    return f.renderText("Login")

def ascii_title5():
    f = Figlet(font='slant')
    return f.renderText("Register")

def menu():
    return f"""
{ascii_title()}
                Welcome User! 
               By: Evan William
"""

def auth_menu():
    return f"""
{ascii_title3()}
                Welcome User!
    Please input your database information:
"""

def cred_menu():
    return f"""
{ascii_title2()}
                Welcome User!
         Please enter your credential:
"""

def register_menu():
    return f"""
{ascii_title5()}
                Welcome User!
         Please enter your credential:
"""

def login_menu():
    return f"""
{ascii_title4()}
                Welcome User!
         Please enter your credential:
"""