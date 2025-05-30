# 📝 Simple Flask Todo App

A minimalistic Todo list web application built with Flask and SQLite.
It lets you **add**, **update**, and **delete** tasks easily through a clean web interface.

---

## 📋 Features

* Add new tasks
* View existing tasks with their creation dates
* Update task content
* Delete tasks
* Simple and clean UI with HTML/CSS
* Data stored in SQLite (`test.db`)

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed
* `Flask` and `Flask_SQLAlchemy` packages

Install dependencies with:

```bash
pip install flask flask_sqlalchemy
```

### How to Run

1. Clone or download the project files, including `app.py`, templates folder (`index.html`, `update.html`, `base.html`), CSS file (`main.css`), and the SQLite database file `test.db` (if already created).

2. If you don’t have `test.db` yet, the app will create it on first run.

3. Run the Flask app:

```bash
python app.py
```

4. Open your browser and go to:

```
http://127.0.0.1:5000/
```

5. Use the web interface to add, update, or delete tasks.

---

## 📁 File Structure

```
/your-project-folder
│
├── app.py                # Main Flask app
├── test.db               # SQLite database file (auto-created if missing)
├── /templates
│   ├── base.html         # Base HTML template
│   ├── index.html        # Main page showing all tasks
│   └── update.html       # Update task form
└── /static
    └── /css
        └── main.css      # Basic styling
```

---

## 🛠️ How It Works

* Flask serves the web pages and handles form submissions.
* SQLAlchemy manages the SQLite database storing tasks.
* Tasks are displayed in a table with creation dates.
* You can delete or update any task via links/buttons in the interface.

---

## 👨‍💻 Developer  
Created by Evan William (2025)  
Version: 1.0
