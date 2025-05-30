# 🧠 Quiz Game with Login System (Python + MySQL)

This is a simple CLI-based Quiz Game built using Python and MySQL. Users can register, log in, and play a 10-question multiple-choice quiz. The app tracks and updates the user’s high score.

---

## 📂 Project Structure

```

quiz-game/
│
├── database.py         # MySQL connection logic
├── main.py             # Main program logic (register, login, play quiz)
├── questions.py        # Quiz questions dictionary
├── queries.sql         # SQL queries used in the app
└── README.md           # You're reading this!

````

---

## 🚀 Features

- ✅ Register with username and password
- 🔐 Login with authentication
- 🧠 Play 10-question quiz (auto-randomized)
- 🏆 Score is calculated based on correct answers
- 💾 High score stored and updated in MySQL database

---

## 🛠️ Setup Instructions

### 1. Install Python 3

Make sure Python 3 is installed. You can check with:

```bash
python --version
````

### 2. Install MySQL Connector for Python

Install the required package using pip:

```bash
pip install mysql-connector-python
```

### 3. Create a MySQL Database

Start your MySQL server and create a new database:

```sql
CREATE DATABASE quizgame;
```

### 4. Create `users` Table

Inside your new database, run this SQL command:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    highscore INT DEFAULT 0
);
```

### 5. Update Database Credentials

Open `database.py` and update the following values with your MySQL credentials:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="quizgame"
)
```

---

## 🎮 Run the Game

Start the program using:

```bash
python main.py
```

Follow the menu to register, login, and play the quiz.

---

## 📝 Notes

* High scores are stored per user.
* All quiz questions and answers are stored in `questions.py`.
* Database interaction uses raw SQL stored in `queries.sql`.

---

## 📌 Future Improvements (Optional Ideas)

* Add password hashing (e.g., using `bcrypt`)
* Build a GUI or web version using Flask
* Add categories or difficulty levels
* Create an admin panel to add/edit questions

---

## 👨‍💻 Developer  
Created by Evan William (2025)  
Version: 1.0
