import requests
import json
import subprocess
import platform
from pyfiglet import Figlet

# MENU PARTS
def ascii_title():
    f = Figlet(font='slant')
    return f.renderText("API-Test")

def ascii_title2():
    f = Figlet(font='doom')
    return f.renderText("Response")

def menu():
    return f"""
{ascii_title()}
                 Welcome User! 
               By: Evan William
"""

def menu2():
    return f"""
{ascii_title2()}
                The Result is Below!
"""

def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

# MAIN PARTS
def main():
    clear_screen()
    print(menu())
    url = input("Enter API's URL: ").strip()
    method = input("Enter method (GET or POST): ").strip().upper()

    headers = {
        "Content-Type": "application/json"
    }

    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        raw_data = input("Enter JSON data for POST (or leave it empty): ").strip()
        try:
            data = json.loads(raw_data) if raw_data else {}
        except json.JSONDecodeError:
            print("Invalid JSON. Exiting...")
            return
        response = requests.post(url, headers=headers, json=data)
    else:
        print("Only GET and POST methods are supported!")
        return

    clear_screen()
    print(menu2())
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:")
        print(json.dumps(response.json(), indent=2))
    except:
        print("Raw Text:")
        print(response.text)
    
    input("\nPress Enter to Start Again...")
    main()

if __name__ == "__main__":
    run_api()
