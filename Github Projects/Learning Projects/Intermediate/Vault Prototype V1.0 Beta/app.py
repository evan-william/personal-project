import sys
import time
from datetime import datetime
from menus import clear_screen, menu
from auth_db import (
    get_db_credentials,
    db_initial_setup,
    load_queries,
    handle_user_auth,
    add_funds_to_balance,
    create_new_commitment,
    get_user_commitments,
    process_expired_commitments,
    update_commitment_status    
)

def main_app_loop(pool, queries, user):
    while True:
        clear_screen()
        
        # Expired Commitments
        try:
            processed_count = process_expired_commitments(pool, queries, user['id'])
            if processed_count > 0:
                print(f"Processed {processed_count} expired commitment(s). Funds moved to donations.")
                time.sleep(2.5)
                clear_screen()
        except Exception as e:
            print(f"Error processing expired commitments: {e}")
            time.sleep(2)
       

        # Refresh user data 
        try:
            conn = pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(queries['find_user_by_id'], (user['id'],))
            current_user_data = cursor.fetchone()
        except Exception as e:
            print(f"An error occurred while fetching user data: {e}")
            time.sleep(2)
            return
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

        if not current_user_data:
            print("Could not retrieve user data. Logging out.")
            time.sleep(2)
            return

        print(menu())  # Main Menu
        print(f"Logged in as: {current_user_data['username']} | Balance: ${current_user_data['balance']:.2f} | Total Donated: ${current_user_data['donation']:.2f}")
        print("\n--- Main Menu ---")
        print("1. Create a new Commitment")
        print("2. View/Manage my Commitments")
        print("3. Add funds to my Balance")
        print("4. Logout")

        choice = input("> ").strip()

        if choice == '1':
            create_commitment_flow(pool, queries, current_user_data)
        elif choice == '2':
            view_commitments_flow(pool, queries, current_user_data)
        elif choice == '3':
            add_funds_flow(pool, queries, current_user_data)
        elif choice == '4':
            print("\nLogging out...")
            time.sleep(1)
            return
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1.5)

def add_funds_flow(pool, queries, user):
    clear_screen()
    print("--- Add Funds to Balance ---")
    print(f"Current Balance: ${user['balance']:.2f}")
    try:
        amount_to_add = float(input("Enter amount to add: $"))
        if amount_to_add <= 0:
            print("\nPlease enter a positive amount.")
            time.sleep(2)
            return

        add_funds_to_balance(pool, queries, user['id'], amount_to_add)
        print(f"\nSuccessfully added ${amount_to_add:.2f} to your balance.")
        time.sleep(2)
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
        time.sleep(2)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        time.sleep(2)

def create_commitment_flow(pool, queries, user):
    clear_screen()
    print("--- Create a New Commitment ---")
    print("Define your goal and set the stakes.")

    task = input("What is the task you want to commit to? > ").strip()
    
    while True:
        try:
            staked_amount = float(input(f"How much will you stake? (Your balance: ${user['balance']:.2f}) > $"))
            if staked_amount <= 0:
                print("Stake must be a positive amount.")
            elif staked_amount > user['balance']:
                print("Stake cannot be greater than your current balance.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    while True:
        deadline_str = input("When is the deadline? (YYYY-MM-DD) > ").strip()
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            if deadline <= datetime.now().date():
                print("Deadline must be in the future.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    witness = input("Who is your witness? (Their name or email) > ").strip()
    charity = input("If you fail, which charity will receive the donation? > ").strip()

    if not all([task, witness, charity]):
        print("\nAll fields must be filled out. Commitment cancelled.")
        time.sleep(2)
        return

    print("\n--- Please Review Your Commitment ---")
    print(f"Task: {task}")
    print(f"Stake: ${staked_amount:.2f}")
    print(f"Deadline: {deadline}")
    print(f"Witness: {witness}")
    print(f"Charity for Donation: {charity}")
    
    confirm = input("\nAre you sure you want to create this commitment? (yes/no) > ").strip().lower()

    if confirm == 'yes':
        try:
            create_new_commitment(pool, queries, user['id'], task, deadline, staked_amount, witness, charity)
            print("\nCommitment created! Skin in the game.")
        except Exception as e:
            print(f"\nFailed to create commitment: {e}")
        time.sleep(2.5)
    else:
        print("\nCommitment cancelled.")
        time.sleep(2)

def view_commitments_flow(pool, queries, user):
    clear_screen()
    print("--- Your Commitments ---")
    try:
        commitments = get_user_commitments(pool, queries, user['id'])
        pending_commitments = [c for c in commitments if c['status'] == 'pending']

        if not commitments:
            print("You have no commitments. Go create one!")
        else:
            for i, comm in enumerate(commitments, 1):
                print(f"\n--- Commitment #{i} (ID: {comm['id']}) ---")
                print(f"  Task: {comm['task']}")
                print(f"  Status: {comm['status'].capitalize()}")
                print(f"  Staked: ${comm['offered_balance']:.2f}")
                print(f"  Deadline: {comm['deadline']}")
                print(f"  Witness: {comm['witness']}")
                print(f"  Donation on Failure: {comm['charity']}")
                print("-" * 25)
        
        if pending_commitments:
            update_choice = input("\nUpdate status of a pending commitment? (yes/no) > ").strip().lower()
            if update_choice == 'yes':
                manage_commitment_status(pool, queries, user, pending_commitments)

    except Exception as e:
        print(f"\nCould not retrieve commitments: {e}")
    
    input("\nPress Enter to return to the main menu...")

def manage_commitment_status(pool, queries, user, pending_commitments):
    try:
        comm_id_to_update = int(input("Enter the ID of the commitment to update: "))
        
        target_commitment = next((c for c in pending_commitments if c['id'] == comm_id_to_update), None)

        if not target_commitment:
            print("Invalid ID or commitment is not pending.")
            time.sleep(2)
            return

        print("\nAs verified by your witness, what is the new status?")
        new_status = input("Enter 'completed' or 'failed': ").strip().lower()

        if new_status not in ['completed', 'failed']:
            print("Invalid status. Please enter 'completed' or 'failed'.")
            time.sleep(2)
            return
        
        update_commitment_status(pool, queries, comm_id_to_update, user['id'], new_status)
        print(f"\nCommitment {comm_id_to_update} has been updated to '{new_status}'.")
        if new_status == 'completed':
            print("Your stake has been refunded to your balance.")
        else:
            print("Your stake has been moved to your donations.")
        time.sleep(3)

    except ValueError:
        print("Invalid ID. Please enter a number.")
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred during the update: {e}")
        time.sleep(2)


def main():
    try:
        queries = load_queries("query.sql")
    except FileNotFoundError:
        print("Error: 'query.sql' not found. Please ensure the file exists.")
        sys.exit(1)

    host, user, password = get_db_credentials()
    pool = db_initial_setup(host, user, password)

    while True:
        logged_in_user = handle_user_auth(pool, queries)
        if logged_in_user:
            main_app_loop(pool, queries, logged_in_user)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Exiting.")
        sys.exit(0)
    finally:
        print("\nVault session ended.")