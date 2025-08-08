from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import random
import google.generativeai as genai
import os
import time
import requests

# Flask app setup
app = Flask(__name__)
# IMPORTANT: Change this to a random, secure key for production
app.secret_key = 'your_secret_key_here'

# Database connection details (stored in session after auth)
# session['db_host']
# session['db_user']
# session['db_password']

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=session.get('db_host', 'localhost'),
            user=session.get('db_user', 'root'),
            password=session.get('db_password', ''),
            database='ai_tik_tak_toe'
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database_and_table(host, user, password):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ai_tik_tak_toe")
        cursor.execute("USE ai_tik_tak_toe")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS wininfo (
                id INT AUTO_INCREMENT PRIMARY KEY,
                UserWin INT NOT NULL DEFAULT 0,
                AiWin INT NOT NULL DEFAULT 0
            )
        """)
        cursor.execute("INSERT IGNORE INTO wininfo (id, UserWin, AiWin) VALUES (1, 0, 0)")
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return False

def get_available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    if ' ' not in board:
        return 'TIE'
    return None

def minimax(board, depth, is_maximizing, ai_symbol, user_symbol):
    winner = check_winner(board)
    if winner == ai_symbol:
        return 10 - depth
    elif winner == user_symbol:
        return depth - 10
    elif winner == 'TIE':
        return 0
    
    available_moves = get_available_moves(board)
    
    if is_maximizing:
        max_score = float('-inf')
        for move in available_moves:
            board[move] = ai_symbol
            score = minimax(board, depth + 1, False, ai_symbol, user_symbol)
            board[move] = ' '
            max_score = max(score, max_score)
        return max_score
    else:
        min_score = float('inf')
        for move in available_moves:
            board[move] = user_symbol
            score = minimax(board, depth + 1, True, ai_symbol, user_symbol)
            board[move] = ' '
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
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def get_ai_move_with_difficulty(board, ai_symbol, user_symbol, difficulty):
    available_moves = get_available_moves(board)
    if not available_moves:
        return None

    if difficulty == "easy":
        if random.random() < 0.3:
            return random.choice(available_moves)
        else:
            return get_best_move(board, ai_symbol, user_symbol)
    elif difficulty == "medium":
        if random.random() < 0.1:
            return random.choice(available_moves)
        else:
            return get_best_move(board, ai_symbol, user_symbol)
    else:  # impossible
        return get_best_move(board, ai_symbol, user_symbol)

def update_win_count(winner_type):
    try:
        conn = get_db_connection()
        if not conn:
            return
        cursor = conn.cursor()
        
        cursor.execute("INSERT IGNORE INTO wininfo (id, UserWin, AiWin) VALUES (1, 0, 0)")
        
        if winner_type == 'USER':
            sql = "UPDATE wininfo SET UserWin = UserWin + 1 WHERE id = 1"
        else:
            sql = "UPDATE wininfo SET AiWin = AiWin + 1 WHERE id = 1"
        
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error updating database: {e}")

@app.route('/', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        host = request.form.get('host', 'localhost')
        user = request.form.get('user', 'root')
        password = request.form.get('password', '')
        api_key = request.form.get('api_key')

        if not api_key:
            flash("Gemini API key is required.", "error")
            return redirect(url_for('auth'))

        session['db_host'] = host
        session['db_user'] = user
        session['db_password'] = password
        session['gemini_api_key'] = api_key

        if not create_database_and_table(host, user, password):
            flash("Database connection failed. Please check your credentials.", "error")
            return redirect(url_for('auth'))

        try:
            genai.configure(api_key=api_key)
            flash("Connection successful!", "success")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error configuring Gemini AI: {str(e)}", "error")
            return redirect(url_for('auth'))
    
    return render_template('auth.html')

@app.route('/menu')
def index():
    if 'db_host' not in session:
        return redirect(url_for('auth'))
    
    return render_template('index.html')

@app.route('/setup', methods=['GET', 'POST'])
def setup_game():
    if 'db_host' not in session:
        return redirect(url_for('auth'))
    
    if request.method == 'POST':
        session['difficulty'] = request.form.get('difficulty', 'impossible')
        session['user_symbol'] = request.form.get('symbol', 'X')
        session['ai_symbol'] = 'O' if session['user_symbol'] == 'X' else 'X'
        
        session['board'] = [' '] * 9
        session['current_player'] = 'USER' if session['user_symbol'] == 'X' else 'AI'
        session['message'] = 'Your turn!' if session['current_player'] == 'USER' else 'AI\'s turn!'
        session['game_over'] = False
        
        return redirect(url_for('play'))
        
    return render_template('setup.html')

@app.route('/play', methods=['GET', 'POST'])
def play():
    if 'db_host' not in session:
        return redirect(url_for('auth'))
    
    if 'board' not in session:
        return redirect(url_for('setup_game'))

    board = session['board'][:]  
    user_symbol = session['user_symbol']
    ai_symbol = session['ai_symbol']
    current_player = session['current_player']
    difficulty = session['difficulty']
    message = session['message']
    game_over = session.get('game_over', False)
    winner = check_winner(board)

    # Handle user move
    if request.method == 'POST' and not game_over and current_player == 'USER':
        move = request.form.get('move')
        if move is not None:
            try:
                move = int(move)
                if 0 <= move <= 8 and board[move] == ' ':
                    board[move] = user_symbol
                    session['board'] = board
                    winner = check_winner(board)
                    
                    if winner:
                        game_over = True
                        if winner == user_symbol:
                            message = "Congratulations! You won!"
                            update_win_count('USER')
                        elif winner == ai_symbol:
                            message = "AI wins this round!"
                            update_win_count('AI')
                        else:
                            message = "It's a tie!"
                    else:
                        current_player = 'AI'
                        message = "AI is thinking..."
                else:
                    message = "Invalid move! Try again."
            except (ValueError, TypeError):
                message = "Invalid move! Try again."

    # Handle AI move
    if not game_over and current_player == 'AI' and not winner:
        ai_move = get_ai_move_with_difficulty(board, ai_symbol, user_symbol, difficulty)
        if ai_move is not None:
            board[ai_move] = ai_symbol
            session['board'] = board
            winner = check_winner(board)
            
            if winner:
                game_over = True
                if winner == user_symbol:
                    message = "Congratulations! You won!"
                    update_win_count('USER')
                elif winner == ai_symbol:
                    message = "AI wins this round!"
                    update_win_count('AI')
                else:
                    message = "It's a tie!"
            else:
                current_player = 'USER'
                message = 'Your turn!'

    # Update session
    session['current_player'] = current_player
    session['message'] = message
    session['game_over'] = game_over
    
    return render_template('play.html', 
                         board=board, 
                         message=message, 
                         user_symbol=user_symbol, 
                         ai_symbol=ai_symbol, 
                         winner=winner, 
                         game_over=game_over)

@app.route('/stats')
def show_win_count():
    if 'db_host' not in session:
        return redirect(url_for('auth'))
        
    try:
        conn = get_db_connection()
        if not conn:
            return "Database connection failed."
            
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT UserWin, AiWin FROM wininfo WHERE id = 1")
        stats = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if not stats:
            stats = {'UserWin': 0, 'AiWin': 0}
        
        user_wins = int(stats['UserWin'])
        ai_wins = int(stats['AiWin'])
        
        total_games = user_wins + ai_wins
        user_percentage = (user_wins / total_games) * 100 if total_games > 0 else 0
        
        return render_template('win_stats.html', stats=stats, total_games=total_games, user_percentage=f"{user_percentage:.1f}")
        
    except Exception as e:
        return f"Error fetching stats: {e}"

@app.route('/reset_game')
def reset_game():
    session.pop('board', None)
    session.pop('current_player', None)
    session.pop('message', None)
    session.pop('game_over', None)
    session.pop('user_symbol', None)
    session.pop('ai_symbol', None)
    session.pop('difficulty', None)
    return redirect(url_for('setup_game'))

if __name__ == '__main__':
    app.run(debug=True)