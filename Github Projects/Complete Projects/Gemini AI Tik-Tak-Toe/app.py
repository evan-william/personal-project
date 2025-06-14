import mysql.connector
from animation import type_text, dot_generate
from menu import menu, clear_screen
from authentication import authentication, create_database_and_table
from query_handling import initiate_query_runner
import time
import inquirer
import sys
import google.generativeai as genai

# Global variables
gemini_model = None

def setup_gemini_ai():
    global gemini_model
    
    while True:
        clear_screen()
        type_text("🤖 Gemini AI Setup\n")
        
        # Get API key from user
        api_key = input("Enter your Gemini API key: ")
        
        try:
            # Configure Gemini AI
            genai.configure(api_key=api_key)
            
            # Test the connection
            dot_generate("Testing Gemini AI connection")
            gemini_model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Simple test prompt
            test_response = gemini_model.generate_content("Say 'Hello' if you're working correctly.")
            
            if test_response and test_response.text:
                type_text("\n✅ Gemini AI connected successfully!\n")
                time.sleep(2)
                return True
            else:
                raise Exception("No response from Gemini AI")
                
        except Exception as e:
            type_text(f"\n❌ Error connecting to Gemini AI: {str(e)}\n")
            
            retry_question = [
                inquirer.List(
                    "retry",
                    message="Would you like to try again?",
                    choices=["Yes", "No"]
                )
            ]
            
            retry_answer = inquirer.prompt(retry_question)
            if retry_answer["retry"] == "No":
                type_text("Exiting application...\n")
                sys.exit(0)

def display_board(board):
    clear_screen()
    type_text("🎮 Tic Tac Toe - You vs Gemini\n")
    type_text("=" * 40 + "\n\n")
    
    # Display board with position numbers
    type_text("   |   |   \n")
    type_text(f" {board[0]} | {board[1]} | {board[2]} \n")
    type_text("___|___|___\n")
    type_text("   |   |   \n")
    type_text(f" {board[3]} | {board[4]} | {board[5]} \n")
    type_text("___|___|___\n")
    type_text("   |   |   \n")
    type_text(f" {board[6]} | {board[7]} | {board[8]} \n")
    type_text("   |   |   \n\n")
    
    # Show position guide
    type_text("Position Guide:\n")
    type_text("1 | 2 | 3\n")
    type_text("4 | 5 | 6\n")
    type_text("7 | 8 | 9\n\n")

def check_winner(board):
    # Winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    
    # Check for tie
    if ' ' not in board:
        return 'TIE'
    
    return None

def get_available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

def minimax(board, depth, is_maximizing, ai_symbol, user_symbol):
    winner = check_winner(board)
    
    # Base cases
    if winner == ai_symbol:
        return 10 - depth  # AI wins (prefer faster wins)
    elif winner == user_symbol:
        return depth - 10  # User wins (prefer slower losses)
    elif winner == 'TIE':
        return 0  # Tie game
    
    available_moves = get_available_moves(board)
    
    if is_maximizing:  # AI's turn
        max_score = float('-inf')
        for move in available_moves:
            board[move] = ai_symbol
            score = minimax(board, depth + 1, False, ai_symbol, user_symbol)
            board[move] = ' '  # Undo move
            max_score = max(score, max_score)
        return max_score
    else:  # User's turn
        min_score = float('inf')
        for move in available_moves:
            board[move] = user_symbol
            score = minimax(board, depth + 1, True, ai_symbol, user_symbol)
            board[move] = ' '  # Undo move
            min_score = min(score, min_score)
        return min_score

def get_best_move(board, ai_symbol, user_symbol):
    available_moves = get_available_moves(board)
    
    if not available_moves:
        return None
    
    best_score = float('-inf')
    best_move = available_moves[0]
    
    for move in available_moves:
        board[move] = ai_symbol
        score = minimax(board, 0, False, ai_symbol, user_symbol)
        board[move] = ' '  # Undo move
        
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move

def get_user_move(board, user_symbol):
    while True:
        try:
            move = input(f"Enter your move (1-9) for '{user_symbol}': ")
            move = int(move) - 1  # Convert to 0-based index
            
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                type_text("❌ Invalid move! Choose an empty position (1-9).\n")
        except ValueError:
            type_text("❌ Please enter a valid number (1-9).\n")

def get_ai_move(board, ai_symbol, user_symbol):
    dot_generate("AI is calculating the perfect move")
    
    # Use minimax algorithm for optimal play for AI
    best_move = get_best_move(board, ai_symbol, user_symbol)
    time.sleep(1)
    
    return best_move

def update_win_count(winner):
    global hostInput, userInput, passwordInput, queries
    
    try:
        conn = mysql.connector.connect(
            host=hostInput,
            user=userInput,
            password=passwordInput,
            database="ai_tik_tak_toe"
        )
        cursor = conn.cursor()
        
        if winner == 'USER':
            sql = queries['save_win_human']
        else:  # AI wins
            sql = queries['save_win_ai']
        
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        type_text(f"Error updating database: {e}\n")

def get_difficulty_level():
    difficulty_question = [
        inquirer.List(
            "difficulty",
            message="Choose AI difficulty level",
            choices=[
                "🟢 Easy (AI makes occasional mistakes)",
                "🟡 Medium (AI plays well but not perfect)", 
                "🔴 Impossible (AI never loses)"
            ]
        )
    ]
    
    difficulty_answer = inquirer.prompt(difficulty_question)
    
    if "Easy" in difficulty_answer["difficulty"]:
        return "easy"
    elif "Medium" in difficulty_answer["difficulty"]:
        return "medium"
    else:
        return "impossible"

def get_ai_move_with_difficulty(board, ai_symbol, user_symbol, difficulty):
    import random
    
    if difficulty == "easy":
        # 30% chance of random move, 70% chance of optimal move
        if random.random() < 0.3:
            available_moves = get_available_moves(board)
            return random.choice(available_moves)
        else:
            return get_best_move(board, ai_symbol, user_symbol)
    
    elif difficulty == "medium":
        # 10% chance of random move, 90% chance of optimal move
        if random.random() < 0.1:
            available_moves = get_available_moves(board)
            return random.choice(available_moves)
        else:
            return get_best_move(board, ai_symbol, user_symbol)
    
    else:  # impossible
        # Always play optimally (100%)
        return get_best_move(board, ai_symbol, user_symbol)

def play():
    clear_screen()
    
    # Choose difficulty
    difficulty = get_difficulty_level()
    
    # Choose symbol
    symbol_question = [
        inquirer.List(
            "symbol",
            message="Choose your symbol",
            choices=["❌ (X)", "⭕ (O)"]
        )
    ]
    
    symbol_answer = inquirer.prompt(symbol_question)
    
    if symbol_answer["symbol"] == "❌ (X)":
        user_symbol = 'X'
        ai_symbol = 'O'
        current_player = 'USER'  # X goes first
    else:
        user_symbol = 'O'
        ai_symbol = 'X'
        current_player = 'AI'    # X goes first
    
    # Initialize board
    board = [' '] * 9
    
    # Show difficulty warning FOR IMPOSSIBLE
    if difficulty == "impossible":
        type_text("\n⚠️  WARNING: You chose IMPOSSIBLE mode!\n")
        type_text("The AI will play perfectly. You can only tie or lose!\n")
        input("Press Enter to accept the challenge...")
    
    # Game loop
    while True:
        display_board(board)
        
        if current_player == 'USER':
            type_text(f"Your turn! You are '{user_symbol}'\n")
            move = get_user_move(board, user_symbol)
            board[move] = user_symbol
            current_player = 'AI'
        else:
            type_text(f"AI's turn! AI is '{ai_symbol}' (Difficulty: {difficulty.upper()})\n")
            move = get_ai_move_with_difficulty(board, ai_symbol, user_symbol, difficulty)
            board[move] = ai_symbol
            type_text(f"AI chose position {move + 1}\n")
            time.sleep(2)
            current_player = 'USER'
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            display_board(board)
            
            if winner == 'TIE':
                type_text("🤝 It's a tie! Good game!\n")
                if difficulty == "impossible":
                    type_text("🎉 Congratulations! Tying against impossible AI is an achievement!\n")
            elif winner == user_symbol:
                type_text("🎉 Congratulations! You won!\n")
                if difficulty == "impossible":
                    type_text("🚨 IMPOSSIBLE! You beat the unbeatable AI!\n")
                elif difficulty == "medium":
                    type_text("👏 Great job beating the medium AI!\n")
                update_win_count('USER')
            else:
                type_text("🤖 AI wins this round!\n")
                if difficulty == "easy":
                    type_text("💪 Try medium or impossible for a real challenge!\n")
                elif difficulty == "medium":
                    type_text("🎯 Good game! Try impossible mode if you dare!\n")
                else:
                    type_text("💀 The AI remains undefeated in impossible mode!\n")
                update_win_count('AI')
            
            # Play again?
            play_again = [
                inquirer.List(
                    "again",
                    message="Play again?",
                    choices=["Yes", "No"]
                )
            ]
            
            again_answer = inquirer.prompt(play_again)
            if again_answer["again"] == "Yes":
                play()  # Recursive call for new game
            break

def show_win_count():
    global hostInput, userInput, passwordInput, queries
    
    # Initiate Connection
    conn = mysql.connector.connect(
        host=hostInput,
        user=userInput,
        password=passwordInput,
        database="ai_tik_tak_toe"
    )
    # Initiate Cursor
    cursor = conn.cursor()
    # Commit Query
    sql = queries['show_win']
    cursor.execute(sql)
    results = cursor.fetchall()
    
    clear_screen()
    
    # Show Win
    if not results:
        type_text("📊 Win Statistics\n")
        type_text("=" * 30 + "\n")
        type_text("No games played yet.\n")
    else:
        type_text("📊 Win Statistics\n")
        type_text("=" * 30 + "\n")
        for each, (id, UserWin, AiWin) in enumerate(results, start=1):
            type_text(f"👤 User Wins: {UserWin}\n")
            type_text(f"🤖 AI Wins: {AiWin}\n")

            # converts str to int (table uses VARCHAR, not Int)
            UserWin = int(UserWin)
            AiWin = int(AiWin)

            total_games = UserWin + AiWin
            if total_games > 0:
                user_percentage = (UserWin / total_games) * 100
                type_text(f"📈 Your Win Rate: {user_percentage:.1f}%\n")
                
                # messages based on win rate
                if user_percentage >= 50:
                    type_text("🏆 Excellent! You're beating the AI more than half the time!\n")
                elif user_percentage >= 25:
                    type_text("💪 Good job! You're holding your own against the AI!\n")
                elif user_percentage >= 10:
                    type_text("🎯 Keep practicing! You're getting better!\n")
                else:
                    type_text("🤖 The AI is dominating! Try easier difficulty levels!\n")
    
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
                choices=["1. Play", "2. Show Win Record", "3. Exit"]
            )
        ]
        answer = inquirer.prompt(questions)
        if answer["choice"] == "1. Play":
            play()
        elif answer["choice"] == "2. Show Win Record":
            show_win_count()
        else:
            dot_generate("Exiting")
            sys.exit(0)

if __name__ == "__main__":
    try:
        # Step 1: Ask for DB Connection
        hostInput, userInput, passwordInput = authentication() 
        
        # Step 2: Create DB & Auth
        create_database_and_table(hostInput, userInput, passwordInput)
        
        # Step 3: Setup Gemini AI (optional now, kept for compatibility)
        setup_gemini_ai()
        
        # Step 4: Load Queries
        queries = initiate_query_runner()
        
        # Step 5: Start Main Menu
        main()
    
    except KeyboardInterrupt:
        type_text("\n\nGoodbye! 👋\n")
        sys.exit(0)
    except Exception as e:
        type_text(f"\nAn error occurred: {e}\n")
        sys.exit(1)