# Quiz Game with Login System

A command-line quiz game built with Python and MySQL to practice database integration and user authentication concepts.

## What It Does

This is a simple terminal-based quiz application I made to learn how to connect Python programs to databases. Users can register accounts, log in, and take a 10-question multiple-choice quiz. The program stores user data and high scores in a MySQL database.

Built this to practice working with databases, user authentication, and organizing a multi-file Python project.

## Features

- User registration and login system
- 10-question multiple-choice quiz with randomized order
- Score tracking and high score storage
- MySQL database integration
- Basic CLI interface

## Project Structure

```
quiz-game/
├── database.py         # Database connection handling
├── main.py            # Main program and menu logic
├── questions.py       # Quiz questions and answers
├── queries.sql        # SQL commands reference
└── README.md          # This file
```

## Requirements

- Python 3.x
- MySQL server
- mysql-connector-python package

Install the Python package:
```bash
pip install mysql-connector-python
```

## Database Setup

Create a MySQL database and table:

```sql
CREATE DATABASE quizgame;

USE quizgame;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    highscore INT DEFAULT 0
);
```

Update your database credentials in `database.py`:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password", 
    database="quizgame"
)
```

## How to Run

Start the program:
```bash
python main.py
```

Follow the menu prompts to register, log in, and play the quiz.

## How It Works

The program has three main parts:
- `main.py` handles the menu system and game flow
- `database.py` manages MySQL connections and queries
- `questions.py` contains the quiz questions as a dictionary

When you play, it randomly selects 10 questions, tracks your score, and updates your high score in the database if you beat your previous best.

## What I Learned

- Connecting Python to MySQL databases
- Basic SQL operations (CREATE, INSERT, SELECT, UPDATE)
- User input validation and menu systems
- Organizing code across multiple files
- Basic authentication (though without proper password hashing)
- Working with dictionaries and random selection

## Known Issues

- Passwords are stored in plain text (not secure)
- No input sanitization for SQL injection prevention
- Basic error handling
- Simple CLI interface only

## Possible Improvements

Could add:
- Password hashing for security
- Better error handling and input validation
- Web interface with Flask
- Question categories or difficulty levels
- Admin panel for managing questions
- Better database security practices

## Author

**Evan William**  
Version 1.0 (2025)

Made this to practice database programming and learn how to build applications that store user data. It was helpful for understanding how desktop applications connect to databases and manage user sessions.

First time working with MySQL in Python, so the code is pretty basic but functional for learning purposes.

---

*Learning project - for fun testing only*
