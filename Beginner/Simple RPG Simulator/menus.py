from pyfiglet import Figlet
import platform
import subprocess

def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def ascii_title1():
    f = Figlet(font='slant')
    return f.renderText("RPG GAME")

def ascii_title2():
    r = Figlet(font='slant')
    return r.renderText("Menu")

def ascii_plains():
    p = Figlet(font= "slant")
    return p.renderText("Plains")

def ascii_grave():
    g = Figlet(font= "slant")
    return g.renderText("Graveyard")

def ascii_cave():
    c = Figlet(font= "slant")
    return c.renderText("Cave")

def menu1():
    return f"""
{ascii_title1()}
                Welcome Player! 
               By: Evan William
"""

def menu2():
    return f"""
{ascii_title2()}
               Choose your action!
"""

def menuplains():
    return f"""
{ascii_plains()}
               Defeat the enemy!
"""

def menugrave():
    return f"""
{ascii_grave()}
               Defeat the enemy!
"""

def menucave():
    return f"""
{ascii_cave()}
               Defeat the enemy!
"""