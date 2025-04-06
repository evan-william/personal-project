import csv
import os
import time
from menus import clear_screen
from logic import startgame

data_folder = "data"
data_file = os.path.join("RPG_SIM", data_folder, "data.csv")
os.makedirs(data_folder, exist_ok=True)

def startregister():
    clear_screen()
    print("======== Register Menu =========")
    username = input("Enter a Username: ")
    password = input("Enter a Password: ")
    print("================================")
    
    with open(data_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[1] == password:
                print(f"Account already exist!")
                time.sleep(2)
                startregister()
            else: 
                with open(data_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([username, password])
                print("\nRegistration successful! You can now log in.")
                time.sleep(2)
                startlogin()

def startlogin():
    clear_screen()
    print("======== Login Menu =========")
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")
    print("================================")
    
    with open(data_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username and row[1] == password:
                print(f"\nWelcome back, {username}! You are now logged in.")
                time.sleep(2)
                startgame()
                return
            
    print("\nInvalid username or password.")
    time.sleep(2)
    startlogin()
