# 💭 Quote Generator

## 📜 Description

A simple Python app that grabs random quotes from the internet and lets you save the good ones to a database. It's got some nice typewriter animations that make reading quotes feel more special.

Perfect for when you need some daily motivation or just want to collect inspiring quotes!

---

## ⚙️ Requirements

- Python **3.7+**
- MySQL running on your computer
- These packages:
  - `mysql-connector-python`
  - `inquirer` 
  - `pyfiglet`
  - `requests`

Install them with:
```bash
pip install mysql-connector-python inquirer pyfiglet requests
```

---

## 📂 Setup

You just need to fix one thing before running:

**In `query_handling.py` around line 10:**
```python
# Change this path to wherever you put the queries.sql file
queries = load_queries(r"YOUR_PATH_HERE\queries.sql")
```

That's it! The app will create the database for you.

---

## ▶️ How To Run

1. Make sure MySQL is running
2. Run this:
```bash
python app.py
```
3. Enter your MySQL info (usually just hit enter for defaults)
4. Start generating quotes!

---

## 🎯 What It Does

- Fetches random quotes from ZenQuotes.io
- Shows them with a cool typewriter effect
- Let's you save favorites to your own database  
- Browse your saved quotes collection
- Clean menus with ASCII art (because why not?)

---

## 🧰 If Something Breaks

| Problem | Fix |
|---------|-----|
| Can't connect to MySQL | Check if MySQL is actually running |
| File path errors | Update that path in query_handling.py |
| No internet quotes | Check your wifi |
| Missing packages | Run the pip install command again |

---

## 🎨 Cool Features

The typewriter animation makes quotes appear letter by letter - it's surprisingly satisfying to watch! Plus there's loading dots and smooth transitions between menus.

The whole thing is built to feel nice to use, not just functional.

---

## 👨‍💻 Developer  
Created by Evan William (2025)  
Version: 1.0
