import mysql.connector
import time

def load_queries(file_path):
    with open(file_path, "r") as file:
        content = file.read().split("-- name:")
        queries = {}
        for each in content:
            if each.strip():
                name, sql = each.strip().split("\n", 1)
                queries[name.strip()] = sql.strip()
        return queries

def ask_for_credentials():
    print("Welcome! Please input your database information below.")
    hostInput = input("host (default: localhost): ").strip() or "localhost"
    userInput = input("user (default: root): ").strip() or "root"
    passwordInput = input("password (default: empty): ").strip() or ""
    return hostInput, userInput, passwordInput

def create_database_and_table(hostInput, userInput, passwordInput):
    conn = mysql.connector.connect(
        host=hostInput,
        user=userInput,
        password=passwordInput
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS myprivateworld")
    cursor.execute("USE myprivateworld")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book_collections (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def main_menu(conn, cursor, queries):
    while True:
        print("\n=== Library Collections Menu ===")
        print("1. Add Collection")
        print("2. Remove Collection by Title")
        print("3. List Collections")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            if title and author:
                add_collection(cursor, conn, queries, title, author)
            else:
                print("Both Title and Author are required.")
        elif choice == "2":
            title = input("Enter Book Title to Remove: ").strip()
            if title:
                remove_collection(cursor, conn, queries, title)
            else:
                print("Title is required.")
        elif choice == "3":
            list_collections(cursor, queries)
        elif choice == "4":
            print("Exiting...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Enter 1, 2, 3 or 4.")

def add_collection(cursor, conn, queries, title, author):
    sql = queries['add_collection']
    cursor.execute(sql, (title, author))
    conn.commit()
    print(f"Collection '{title}' by {author} added successfully.")

def remove_collection(cursor, conn, queries, title):
    sql = queries['remove_collection']
    cursor.execute(sql, (title,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Collection '{title}' removed successfully.")
    else:
        print(f"No collection found with title '{title}'.")

def list_collections(cursor, queries):
    sql = queries['list_collections']
    cursor.execute(sql)
    collections = cursor.fetchall()
    print("\nCollections in library:")
    if not collections:
        print("  (No collections found)")
    for col in collections:
        print(f"  ID: {col[0]} | Title: {col[1]} | Author: {col[2]}")
    print()

if __name__ == "__main__":
    # Ask user credentials with defaults already being set (FILL WITH EMPTY FOR DEFAULT)
    hostInput, userInput, passwordInput = ask_for_credentials()

    # Create database and table automatically after being set 
    create_database_and_table(hostInput, userInput, passwordInput)

    # Load queries from your SQL file {Can change this to ur sql path if u want}
    queries = load_queries(r"D:\College\Programming Files\Codes\Projects\Learning Projects\Book Storage Python + SQL\queries.sql")

    # Connect to the database using entered credentials from the USER INPUT
    conn = mysql.connector.connect(
        host=hostInput,
        user=userInput,
        password=passwordInput,
        database="myprivateworld"
    )
    cursor = conn.cursor()

    main_menu(conn, cursor, queries)

    cursor.close()
    conn.close()
