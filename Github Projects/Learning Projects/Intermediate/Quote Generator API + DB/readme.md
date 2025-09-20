# Quote Generator

A Python application that fetches inspirational quotes from an API and stores favorites in a MySQL database with typewriter-style display animations.

## What It Does

This is a terminal-based quote generator I built to practice API integration and database operations. The app pulls random quotes from ZenQuotes API, displays them with a typewriter animation effect, and lets users save their favorites to a local MySQL database for later viewing.

Built this to learn how to work with external APIs, implement visual effects in CLI applications, and manage user data persistence.

## Features

* Fetches random quotes from ZenQuotes.io API
* Typewriter animation for quote display
* Save favorite quotes to MySQL database
* Browse saved quotes collection
* ASCII art menus and loading animations
* Basic error handling for network issues

## Project Structure

```
quote-generator/
├── app.py              # Main application entry point
├── query_handling.py   # Database operations and SQL queries
├── queries.sql         # SQL schema and commands
└── README.md          # This file
```

## Requirements

* Python 3.7+
* MySQL server
* Internet connection for API calls
* Required packages:
  - mysql-connector-python
  - inquirer
  - pyfiglet
  - requests

Install the packages:

```bash
pip install mysql-connector-python inquirer pyfiglet requests
```

## Database Setup

The application will create the database automatically, but you need to update the file path in `query_handling.py`:

```python
# Line 10 in query_handling.py - update this path
queries = load_queries(r"C:\path\to\your\queries.sql")
```

Make sure your MySQL server is running before starting the application.

## How to Run

Start the program:

```bash
python app.py
```

Enter your MySQL credentials when prompted (usually localhost with your MySQL username/password). The app will handle database creation and table setup automatically.

## How It Works

The application has two main components:
* `app.py` manages the user interface, API calls, and display animations
* `query_handling.py` handles all database connections and SQL operations

When you generate a quote, it makes an HTTP request to ZenQuotes API, displays the quote with a typewriter effect, and gives you options to save it or get another one. Saved quotes are stored in a local MySQL database for browsing later.

## What I Learned

* Making HTTP requests to external APIs
* Implementing visual effects in terminal applications
* Managing database connections and queries
* Handling JSON response data
* Creating interactive CLI menus with inquirer
* Error handling for network and database operations
* Working with external Python libraries

## Known Issues

* No offline mode when API is unavailable
* Basic error handling for database failures
* Requires manual path configuration
* Simple menu system only
* No quote categorization or search

## Possible Improvements

Could add:
* Offline quote database as fallback
* Better error recovery and retry logic
* Quote search and filtering options
* Export saved quotes to text files
* Multiple quote source APIs
* Configuration file for settings
* Quote sharing functionality

## Author

**Evan William** - Version 1.0 (2025)

Created this while learning API integration and database programming. It was a good project for understanding how to combine external data sources with local storage and create engaging user interfaces in terminal applications.

First time working with the ZenQuotes API and implementing typewriter effects, so the code is straightforward but functional for learning purposes.

*Learning project - focuses on core concepts of understanding APIs*
