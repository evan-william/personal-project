import mysql.connector
from animation import type_text, dot_generate
from menu import menu, clear_screen
from quote_generator import generate_quote
from authentication import authentication, create_database_and_table
from query_handling import initiate_query_runner
import time
import inquirer
import sys

def start_quote():
    content, author = generate_quote()
    print("Quote: ",end="") 
    type_text(content)

    print("\nAuthor: ",end="")
    type_text(author)

    while True:
        action = input("\nSave Quote [Y/N]: ")
        if action == "Y":
            # Initiate Connection
            conn = mysql.connector.connect(
            host=hostInput,
            user=userInput,
            password=passwordInput,
            database="quotesgen"
            )

            # Initiate Cursor
            cursor = conn.cursor()

            # Commit Query
            sql = queries['save_quote']
            cursor.execute(sql, (content, author))
            conn.commit()
            
            # Close Connection
            cursor.close()
            conn.close()

            print("\nQuotes & Author Saved!")
            time.sleep(0.3)
            dot_generate("Returning")

            break

        elif action == "N":
            return
        else:
            print("Invalid Input!")

def show_saved():
    # Initiate Connection
    conn = mysql.connector.connect(
    host=hostInput,
    user=userInput,
    password=passwordInput,
    database="quotesgen"
    )

    # Initiate Cursor
    cursor = conn.cursor()

    # Commit Query
    sql = queries['show_saved_quote']
    cursor.execute(sql)
    results = cursor.fetchall()

    # Show Quotes
    if not results:
        print("\nNo saved quotes found.")
    else:
        print("\n--- Saved Quotes ---")
        for each, (id, content, author) in enumerate(results, start=1):
            print(f"{each}. \"{content}\" - {author}")
        input("\nPress Enter to return to menu...")

    # Close Connection
    cursor.close()
    conn.close()

def main():
    while True:
        clear_screen()
        print(menu())
        questions = [
            inquirer.List(
                "choice",
                message="Choose an option",
                choices=["1. Generate Quote", "2. Show Saved Quote", "3. Exit"]
            )
        ]

        answer = inquirer.prompt(questions)
        if answer["choice"] == "1. Generate Quote":
            start_quote()
        elif answer["choice"] == "2. Show Saved Quote":
            show_saved()
        else:
            dot_generate("Exiting")
            sys.exit(0)

if __name__ == "__main__":
    # Step 1: Ask for DB Connection
    hostInput, userInput, passwordInput = authentication() 

    # Step 2: Create DB & Auth
    create_database_and_table(hostInput, userInput, passwordInput)

    # Step 3: If Success, Open Main Menu & Load Query
    queries = initiate_query_runner()
    main()


    
    