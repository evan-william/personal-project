import time
import mysql.connector
from mysql.connector import pooling
import sys
import bcrypt
from getpass import getpass

from menus import auth_menu, cred_menu, clear_screen
from animations import dot_generate

def db_initial_setup(hostInput, userInput, passwordInput):
    try:
        # First, connect to create the database if it doesn't exist
        temp_conn = mysql.connector.connect(
            host=hostInput,
            user=userInput,
            password=passwordInput
        )
        cursor = temp_conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS VaultPrototype")
        cursor.close()
        temp_conn.close()

        # Now, create a connection pool for the application to use
        pool = pooling.MySQLConnectionPool(
            pool_name="vault_pool",
            pool_size=5,
            host=hostInput,
            user=userInput,
            password=passwordInput,
            database="VaultPrototype"
        )
        print("\nDatabase connection pool created successfully!")

        # Use a connection from the pool to set up tables
        conn = pool.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS User (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                donation DECIMAL(10, 2) NOT NULL DEFAULT 0.00
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Sessions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                task VARCHAR(255) NOT NULL,
                deadline DATE NOT NULL,
                offered_balance DECIMAL(10, 2) NOT NULL,
                witness VARCHAR(255) NOT NULL,
                status ENUM('pending', 'completed', 'failed') DEFAULT 'pending',
                charity VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES User(id)
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        
        time.sleep(1.5)
        return pool

    except mysql.connector.Error as err:
        print(f"\nDatabase connection failed: {err}")
        dot_generate("Exiting")
        print()
        sys.exit(0)

def get_db_credentials():
    clear_screen()
    print(auth_menu())
    hostInput = input("Host (default: localhost): ").strip() or "localhost"
    userInput = input("User (default: root): ").strip() or "root"
    passwordInput = getpass("Password (default: empty, hidden input): ").strip() or ""
    return hostInput, userInput, passwordInput

def load_queries(file_path):
    with open(file_path, "r") as file:
        content = file.read().split("-- name:")
        queries = {}
        for each in content:
            part = each.strip()
            if part and '\n' in part:
                name, sql = part.split("\n", 1)
                queries[name.strip()] = sql.strip()
        return queries

# --- Password Hashing Utilities ---
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# --- User Authentication Functions (Modified for Pooling) ---
def register_user(pool, queries):
    clear_screen()
    print(cred_menu())
    print("--- Register New User ---")
    username = input("Enter a new username: ").strip()
    password = getpass("Enter a password: ").strip()

    if not username or not password:
        print("\nUsername and password cannot be empty.")
        time.sleep(2)
        return

    try:
        hashed_pw = hash_password(password)
        conn = pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(queries['register_new_user'], (username, hashed_pw))
        conn.commit()
        print(f"\nUser '{username}' created successfully!")
        dot_generate("Returning to menu")
    except mysql.connector.IntegrityError:
        print(f"\nUsername '{username}' already exists. Please try another.")
        time.sleep(2)
    except mysql.connector.Error as err:
        print(f"\nAn error occurred: {err}")
        time.sleep(2)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def login_user(pool, queries):
    clear_screen()
    print(cred_menu())
    print("--- User Login ---")
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()

    try:
        conn = pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(queries['find_user_by_username'], (username,))
        user_record = cursor.fetchone()

        if user_record and check_password(password, user_record['password']):
            print("\nLogin successful!")
            dot_generate(f"Welcome, {username}")
            return user_record
        else:
            print("\nInvalid username or password.")
            time.sleep(2)
            return None
    except mysql.connector.Error as err:
        print(f"\nAn error occurred: {err}")
        time.sleep(2)
        return None
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def handle_user_auth(pool, queries):
    logged_in_user = None
    while not logged_in_user:
        clear_screen()
        print(cred_menu())
        choice = input("Choose an option:\n1. Login\n2. Register\n3. Exit\n> ").strip()

        if choice == '1':
            logged_in_user = login_user(pool, queries)
        elif choice == '2':
            register_user(pool, queries)
        elif choice == '3':
            print("\nExiting application.")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1.5)
    return logged_in_user

# --- Application Core Functions (Modified for Pooling) ---
def add_funds_to_balance(pool, queries, user_id, amount):
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(queries['add_to_balance'], (amount, user_id))
        conn.commit()
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def create_new_commitment(pool, queries, user_id, task, deadline, stake, witness, charity):
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()
        conn.start_transaction()
        cursor.execute(queries['add_to_balance'], (-stake, user_id))
        cursor.execute(queries['start_session'], (user_id, task, deadline, stake, witness, charity))
        conn.commit()
    except mysql.connector.Error as err:
        if 'conn' in locals() and conn.is_connected():
            conn.rollback()
        raise err
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def get_user_commitments(pool, queries, user_id):
    try:
        conn = pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(queries['get_sessions_by_user'], (user_id,))
        commitments = cursor.fetchall()
        return commitments
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# ---  Expired Func For Data ---

def process_expired_commitments(pool, queries, user_id):
    conn = None
    try:
        conn = pool.get_connection()
        
        # Step 1: Read data with a dedicated cursor
        read_cursor = conn.cursor(dictionary=True)
        read_cursor.execute(queries['get_expired_pending_sessions_by_user'], (user_id,))
        expired_sessions = read_cursor.fetchall()
        read_cursor.close() # Close the read cursor immediately

        if not expired_sessions:
            return 0

        # Step 2: Perform write operations with a new, clean cursor
        conn.start_transaction()
        write_cursor = conn.cursor()
        for session in expired_sessions:
            # Mark as failed
            write_cursor.execute(queries['update_session_status'], ('failed', session['id']))
            # Add stake to user's donation total
            write_cursor.execute(queries['add_to_donation'], (session['offered_balance'], user_id))
        
        conn.commit()
        write_cursor.close()
        return len(expired_sessions)

    except mysql.connector.Error as err:
        if conn and conn.is_connected():
            conn.rollback()
        raise err
    finally:
        if conn and conn.is_connected():
            conn.close()

def update_commitment_status(pool, queries, session_id, user_id, new_status):
    conn = None
    try:
        conn = pool.get_connection()
        conn.start_transaction()

        # Step 1: Read data with a dedicated cursor
        read_cursor = conn.cursor(dictionary=True)
        read_cursor.execute(queries['get_session_by_id'], (session_id,))
        session = read_cursor.fetchone()
        read_cursor.close() # Close the read cursor immediately
        
        if not session:
            raise ValueError("Commitment not found.")
        
        stake = session['offered_balance']

        # Step 2: Perform write operations with a new, clean cursor
        write_cursor = conn.cursor()
        # Update the session status
        write_cursor.execute(queries['update_session_status'], (new_status, session_id))

        if new_status == 'completed':
            # Refund the stake to the user's balance
            write_cursor.execute(queries['add_to_balance'], (stake, user_id))
        elif new_status == 'failed':
            # Add the stake to the user's donation total
            write_cursor.execute(queries['add_to_donation'], (stake, user_id))
        
        conn.commit()
        write_cursor.close()

    except mysql.connector.Error as err:
        if conn and conn.is_connected():
            conn.rollback()
        raise err
    finally:
        if conn and conn.is_connected():
            conn.close()