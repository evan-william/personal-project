# Simple Flask Todo App

A minimalistic web-based todo list application built with Flask and SQLite for managing daily tasks through a clean browser interface.

## What It Does

This is a basic todo list web app I created to learn Flask web development and database integration. Users can add new tasks, view them with creation timestamps, edit existing tasks, and delete completed ones. All data is stored locally in an SQLite database file.

Built this to practice web development fundamentals, template rendering, and CRUD operations with Flask-SQLAlchemy.

## Features

* Add new tasks with automatic timestamp recording
* View all tasks in a clean table format
* Update existing task content
* Delete completed or unwanted tasks
* Responsive web interface with custom CSS
* SQLite database for persistent storage
* Flask templating with Jinja2

## Project Structure

```
flask-todo-app/
├── app.py              # Main Flask application
├── test.db             # SQLite database (auto-created)
├── templates/
│   ├── base.html       # Base template with common layout
│   ├── index.html      # Main task listing page
│   └── update.html     # Task editing form
├── static/
│   └── css/
│       └── main.css    # Custom styling
└── README.md           # This file
```

## Requirements

* Python 3.x
* Flask web framework
* Flask-SQLAlchemy for database operations

Install the required packages:

```bash
pip install flask flask_sqlalchemy
```

## Database Setup

The application automatically creates the SQLite database and tables on first run. No manual database setup is required.

## How to Run

Start the Flask development server:

```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

Use the web interface to manage your tasks.

## How It Works

The application follows a simple MVC pattern:
* `app.py` contains the Flask routes and database models
* Templates handle the presentation layer with Jinja2 templating
* SQLAlchemy manages database operations and data persistence
* Static files provide custom styling for the interface

Each task is stored with an ID, content, and creation timestamp. The interface provides forms for adding new tasks and updating existing ones.

## What I Learned

* Flask web application structure and routing
* Template inheritance with Jinja2
* Database modeling with SQLAlchemy
* HTML form handling and POST requests
* Static file serving in Flask
* Basic CRUD operations in web applications
* Database migrations and table creation

## Known Issues

* No user authentication or session management
* Basic error handling for database operations
* Simple styling without responsive design considerations
* No data validation on task input
* SQLite limitations for concurrent users

## Possible Improvements

Could add:
* User registration and authentication system
* Task categories or priority levels
* Due dates and reminder functionality
* Better responsive design with Bootstrap
* Task search and filtering options
* Data export and import capabilities
* API endpoints for mobile app integration

## Author

**Evan William** - Version 1.0 (2025)

Created this as my first Flask web application to understand the basics of web development with Python. It helped me learn how to structure web apps, work with databases, and create interactive user interfaces.

First time building a complete web application, so the code focuses on core functionality rather than advanced features.

*Learning project - demonstrates fundamental Flask concepts for todo list management.*
