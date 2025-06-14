from menu import auth_menu, clear_screen
import mysql.connector
import time
import sys

def create_database_and_table(hostInput, userInput, passwordInput):
        try:
            conn = mysql.connector.connect(
                host=hostInput,
                user=userInput,
                password=passwordInput
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS ai_tik_tak_toe")
            cursor.execute("USE ai_tik_tak_toe")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS wininfo (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    UserWin VARCHAR(255) NOT NULL,
                    AiWin VARCHAR(255) NOT NULL
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()

            print("\nConnected Succesfully!")
            time.sleep(1)
            for i in range(4):
                dots = "." * i
                print(f"\rOpening Main Menu{dots}   ", end='', flush=True)
                time.sleep(0.5)
            time.sleep(0.5)
            
        except mysql.connector.errors.DatabaseError:
             print("\nDatabase connection failed!")
             time.sleep(1)
             for i in range(4):
                dots = "." * i
                print(f"\rExiting{dots}   ", end='', flush=True)
                time.sleep(0.5)

             print()  
             sys.exit(0)

def authentication():
    clear_screen()
    print(auth_menu())
    hostInput = input("Host (default: localhost): ").strip() or "localhost"
    userInput = input("User (default: root): ").strip() or "root"
    passwordInput = input("Password (default: empty): ").strip() or ""
    return hostInput, userInput, passwordInput

