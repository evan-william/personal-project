from authentication import authentication, create_database_and_table
from menu import clear_screen, ascii_title, ascii_title2, ascii_title3, menu, cred_menu, register_menu, login_menu
import inquirer
import sys
import time
import mysql.connector
import random

current_username = None
current_highscore = None

# Quiz questions dictionary
quiz_questions = {
    1: {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C",
        "points": 10
    },
    2: {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B",
        "points": 10
    },
    3: {
        "question": "What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B",
        "points": 5
    },
    4: {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Van Gogh", "B. Picasso", "C. Da Vinci", "D. Michelangelo"],
        "answer": "C",
        "points": 15
    },
    5: {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D",
        "points": 10
    },
    6: {
        "question": "Which programming language is known for web development?",
        "options": ["A. C++", "B. JavaScript", "C. Assembly", "D. COBOL"],
        "answer": "B",
        "points": 10
    },
    7: {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C",
        "points": 10
    },
    8: {
        "question": "Which country is home to the kangaroo?",
        "options": ["A. New Zealand", "B. Australia", "C. South Africa", "D. Brazil"],
        "answer": "B",
        "points": 10
    },
    9: {
        "question": "What does 'HTTP' stand for?",
        "options": ["A. HyperText Transfer Protocol", "B. High Tech Transfer Protocol", 
                   "C. HyperText Terminal Protocol", "D. Home Transfer Text Protocol"],
        "answer": "A",
        "points": 15
    },
    10: {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Silver", "D. Iron"],
        "answer": "B",
        "points": 10
    },
    11: {
        "question": "What is the tallest mountain in the world?",
        "options": ["A. K2", "B. Kangchenjunga", "C. Mount Everest", "D. Lhotse"],
        "answer": "C",
        "points": 10
    },
    12: {
        "question": "Which language has the most native speakers worldwide?",
        "options": ["A. English", "B. Spanish", "C. Hindi", "D. Mandarin Chinese"],
        "answer": "D",
        "points": 15
    },
    13: {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B",
        "points": 10
    },
    14: {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Hydrogen", "C. Carbon Dioxide", "D. Nitrogen"],
        "answer": "C",
        "points": 10
    },
    15: {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["A. China", "B. Brazil", "C. United Kingdom", "D. Russia"],
        "answer": "B",
        "points": 10
    }
}

def check_username_exists(username):
    # Check Dupe Username
    conn = mysql.connector.connect(
        host=hostInput,
        user=userInput,
        password=passwordInput,
        database="simplequiz"
    )
    cursor = conn.cursor()
    
    try:
        sql = "SELECT COUNT(*) FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        exists = result[0] > 0
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        exists = False
    finally:
        cursor.close()
        conn.close()
    
    return exists

def remove_duplicate_usernames():
    # Remove Dupe Username, Keep the highestscore
    conn = mysql.connector.connect(
        host=hostInput,
        user=userInput,
        password=passwordInput,
        database="simplequiz"
    )
    cursor = conn.cursor()
    
    try:
        # Find duplicates and keep only the one with highest score
        sql = """
        DELETE u1 FROM users u1
        INNER JOIN users u2 
        WHERE u1.username = u2.username 
        AND (u1.highscore < u2.highscore 
             OR (u1.highscore = u2.highscore AND u1.id > u2.id))
        """
        cursor.execute(sql)
        deleted_count = cursor.rowcount
        conn.commit()
        
        if deleted_count > 0:
            print(f"Removed {deleted_count} duplicate username(s) from database.")
        
    except mysql.connector.Error as err:
        print(f"Error removing duplicates: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def startregister():
    clear_screen()
    print(register_menu())

    while True:  # Loop until successful registration
        registerNameInput = input("Enter your username: ").strip()
        
        # Check if username is empty
        if not registerNameInput:
            print("Username cannot be empty! Please try again.\n")
            continue
            
        # Check if username already exists
        if check_username_exists(registerNameInput):
            print(f"Username '{registerNameInput}' already exists! Please choose a different username.\n")
            continue
            
        # Username is valid, get password
        registerPassInput = input("Enter your password: ").strip()
        
        # Check if password is empty
        if not registerPassInput:
            print("Password cannot be empty! Please try again.\n")
            continue
            
        # Proceed with registration
        conn = mysql.connector.connect(
            host=hostInput,
            user=userInput,
            password=passwordInput,
            database="simplequiz"
        )
        cursor = conn.cursor()
        
        try:
            # Username & Pass Registered
            sql = queries['register_input']
            cursor.execute(sql, (registerNameInput, registerPassInput, 0))
            conn.commit()
            print(f"\nSuccessfully registered username '{registerNameInput}'!")
            print("You can now login with your credentials.")
            
            # Wait before returning to menu
            time.sleep(2)
            break  # Exit the loop after successful registration
            
        except mysql.connector.IntegrityError as err:
            if "Duplicate entry" in str(err):
                print(f"Username '{registerNameInput}' already exists! Please choose a different username.\n")
            else:
                print(f"Registration error: {err}\n")
        except mysql.connector.Error as err:
            print(f"Database error: {err}\n")
        finally:
            cursor.close()
            conn.close()
            login_Register()
            
def startlogin():
    clear_screen()
    print(login_menu())
 
    # Open Connect
    conn = mysql.connector.connect(
                host=hostInput,
                user=userInput,
                password=passwordInput,
                database="simplequiz"
               )

    cursor = conn.cursor()

    loginNameInput = input("Enter your username: ").strip()
    loginPassInput = input("Enter your password: ")

    try:
        # Using queries dictionary (add the query to your queries.sql file)
        sql = queries['login_input']
        cursor.execute(sql, (loginNameInput, loginPassInput))
        result = cursor.fetchone()
        
        # Consume any remaining results
        cursor.fetchall()  # This ensures all results are consumed
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        cursor.close()
        conn.close()
        return
    
    finally:
        cursor.close()
        conn.close()

    if result:
        # Login successful
        username = result[0]
        highscore = result[1]
        print(f"\nLogin successful! Welcome back, {username}!")
        print(f"Your current high score is: {highscore}")
        
        # Store current user info
        global current_username, current_highscore
        current_username = username
        current_highscore = highscore

        for i in range(4):
                dots = "." * i
                print(f"\rOpening Quiz Menu{dots}   ", end='', flush=True)
                time.sleep(0.5)
        time.sleep(2)

        main_menu()
        
    else:
        # Login failed
        print("\nInvalid username or password!")
        time.sleep(2)
        login_Register()

def get_current_user():
    return current_username, current_highscore

def update_highscore(new_score):
    global current_highscore
    if new_score > current_highscore:
        conn = mysql.connector.connect(
            host=hostInput,
            user=userInput,
            password=passwordInput,
            database="simplequiz"
        )
        cursor = conn.cursor()
        
        sql = "UPDATE users SET highscore = %s WHERE username = %s"
        cursor.execute(sql, (new_score, current_username))
        conn.commit()
        
        current_highscore = new_score
        print(f"New high score: {new_score}!")
        
        cursor.close()
        conn.close()

def get_current_highscore():
    conn = mysql.connector.connect(
        host=hostInput,
        user=userInput,
        password=passwordInput,
        database="simplequiz"
    )
    cursor = conn.cursor()
    
    sql = "SELECT highscore FROM users WHERE username = %s"
    cursor.execute(sql, (current_username,))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return result[0] if result else 0

def display_question(question_num, question_data):
    print(f"\n=== Question {question_num} ===")
    print(f"Points: {question_data['points']}")
    print(f"\n{question_data['question']}")
    print()
    for option in question_data['options']:
        print(option)
    print()

def get_user_answer():
    while True:
        answer = input("Your answer (A/B/C/D): ").upper().strip()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        elif answer == 'Z':
            for i in range(4):
                dots = "." * i
                print(f"\rExit Shortcut Used{dots}   ", end='', flush=True)
                time.sleep(0.5)
            sys.exit(0)
        else:
            print("Please enter a valid option (A, B, C, or D)")

def quiz(current_username, current_highscore):
    clear_screen()
    print(ascii_title3())  
    print(f"Welcome to the Quiz, {current_username}!")
    print(f"Your current high score: {current_highscore}")
    print("\nInstructions:")
    print("- Answer each question by typing A, B, C, or D")
    print("- Each question has different point values")
    print("- Try to beat your high score!")
    
    input("\nPress Enter to start the quiz...")
    
    current_score = 0
    correct_answers = 0
    total_questions = len(quiz_questions)
    
    # Shuffle questions for variety
    question_order = list(quiz_questions.keys())
    random.shuffle(question_order)
    
    for i, question_num in enumerate(question_order, 1):
        clear_screen()
        question_data = quiz_questions[question_num]
        
        # Show progress
        print(f"Progress: {i}/{total_questions}")
        print(f"Current Score: {current_score}")
        print("="*50)
        
        # Display question
        display_question(i, question_data)
        
        # Get user answer
        user_answer = get_user_answer()
        
        # Check if answer is correct
        if user_answer == question_data['answer']:
            points_earned = question_data['points']
            current_score += points_earned
            correct_answers += 1
            print(f"\n✓ Correct! You earned {points_earned} points!")
        else:
            correct_option = question_data['answer']
            print(f"\n✗ Wrong! The correct answer was {correct_option}")
        
        # Show current progress
        print(f"Score: {current_score}")
        
        if i < total_questions:
            input("Press Enter to continue...")
    
    # Quiz finished - show results
    show_quiz_results(current_username, current_score, correct_answers, total_questions, current_highscore)

def show_quiz_results(username, final_score, correct_answers, total_questions, old_highscore):
    clear_screen()
    print("="*60)
    print("🎉 QUIZ COMPLETED! 🎉")
    print("="*60)
    print(f"Player: {username}")
    print(f"Questions Answered: {total_questions}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Accuracy: {(correct_answers/total_questions)*100:.1f}%")
    print(f"Final Score: {final_score}")
    print(f"Previous High Score: {old_highscore}")
    
    # Check if new high score
    if final_score > old_highscore:
        print("\n🏆 NEW HIGH SCORE!! 🏆")
        print(f"You beat your previous record by {final_score - old_highscore} points!")
        update_highscore(final_score)
    elif final_score == old_highscore:
        print("\n🎯 You tied your high score!")
    else:
        points_needed = old_highscore - final_score
        print(f"\n📈 You need {points_needed} more points to beat your high score!")
    
    # Performance feedback
    accuracy = (correct_answers/total_questions) * 100
    if accuracy >= 90:
        print("\n🌟 Excellent performance!")
    elif accuracy >= 70:
        print("\n👍 Good job!")
    elif accuracy >= 50:
        print("\n👌 Not bad, keep practicing!")
    else:
        print("\n💪 Keep studying and try again!")
    
    print("\nWhat would you like to do next?")
    while True:
        choice = input("1. Play Again\n2. Main Menu\n3. Exit\nChoice (1-3): ").strip()
        if choice == "1":
            quiz(current_username, get_current_highscore())
            break
        elif choice == "2":
            main_menu()
            break
        elif choice == "3":
            for i in range(4):
                dots = "." * i
                print(f"\rThanks for playing! Goodbye{dots}   ", end='', flush=True)
                time.sleep(0.5)
            time.sleep(0.5)
            sys.exit(0)
        else:
            print("\nPlease enter 1, 2, or 3")

def main_menu():
    # Main Menu
    clear_screen()
    print(menu())
    print(f"Welcome, {current_username}!")
    print(f"High Score: {current_highscore}\n")
    
    questions = [
        inquirer.List(
            "choice",
            message="What would you like to do?",
            choices=["Start Quiz", "View Leaderboard", "Logout"]
        )
    ]
    answer = inquirer.prompt(questions)
    
    if answer["choice"] == "Start Quiz":
        quiz(current_username, current_highscore)
    elif answer["choice"] == "View Leaderboard":
        view_leaderboard()
    else:
        for i in range(4):
                dots = "." * i
                print(f"\rLogging out{dots}   ", end='', flush=True)
                time.sleep(0.5)
        time.sleep(1)
        login_Register()

def view_leaderboard():
    # View Top 10
    clear_screen()
    print("🏆 LEADERBOARD 🏆")
    print("="*40)
    
    conn = mysql.connector.connect(
        host=hostInput,
        user=userInput,
        password=passwordInput,
        database="simplequiz"
    )
    cursor = conn.cursor()
    
    sql = "SELECT username, highscore FROM users ORDER BY highscore DESC LIMIT 10"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    if results:
        for i, (username, score) in enumerate(results, 1):
            if username == current_username:
                print(f"{i:2d}. {username:<15} - {score:>5} points ⭐ (You)")
            else:
                print(f"{i:2d}. {username:<15} - {score:>5} points")
    else:
        print("No scores recorded yet!")
    
    cursor.close()
    conn.close()
    
    input("\nPress Enter to return to main menu...")
    main_menu()

def load_queries(file_path):
    with open(file_path, "r") as file:
        content = file.read().split("-- name:")
        queries = {}
        for each in content:
            if each.strip():
                name, sql = each.strip().split("\n", 1) 
                queries[name.strip()] = sql.strip()
        return queries

def login_Register():
    clear_screen()
    print(cred_menu())
    questions = [
        inquirer.List(
                "choice",
                message="Choose an option",
                choices=["Register", "Login", "Clean Database", "Exit"]
            )
        ]
    answer = inquirer.prompt(questions)
    if answer["choice"] == "Register":
        startregister()
    elif answer["choice"] == "Login":
        startlogin()
    elif answer["choice"] == "Clean Database":
        print("Cleaning duplicate usernames from database...")
        remove_duplicate_usernames()
        print("Database cleanup completed!")
        time.sleep(2)
        login_Register()
    else:
        for i in range(4):
                dots = "." * i
                print(f"\rExiting{dots}   ", end='', flush=True)
                time.sleep(0.5)
        time.sleep(2)
        sys.exit(0)

if __name__ == "__main__":
    # (1) Ask for Credential and Print Login Menu
    hostInput, userInput, passwordInput = authentication()

    # (2) Create DB
    create_database_and_table(hostInput, userInput, passwordInput)

    # (3) Load Login Menu & Query & Start App 
    queries = load_queries(r"D:\College\Programming Files\Codes\Projects\Learning Projects\Quiz App Python + SQL\queries.sql")
    login_Register()