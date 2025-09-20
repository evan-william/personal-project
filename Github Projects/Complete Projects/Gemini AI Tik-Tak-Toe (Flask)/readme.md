# AI Tic Tac Toe - Flask Gemini Edition

A web-based Tic Tac Toe game with an unbeatable AI opponent built using Flask, featuring the minimax algorithm and MySQL database integration for game statistics.

## What It Does

This is the web version of my AI Tic Tac Toe game, rebuilt with Flask to provide a browser-based gaming experience. Players can challenge an AI opponent that uses the minimax algorithm to make optimal moves, with three difficulty levels ranging from beatable to mathematically impossible to defeat.

Built this to learn web development with Flask, practice full-stack development, and understand how to migrate command-line applications to web interfaces.

## Features

* Web-based Tic Tac Toe with responsive click-to-play interface
* Minimax algorithm AI that never loses on highest difficulty
* Three difficulty levels: Easy, Medium, and Impossible
* MySQL database integration for persistent game statistics
* Session management for maintaining game state
* Real-time move validation and game outcome detection
* Clean web interface with custom CSS styling
* Google Gemini API integration for enhanced features

## Project Structure

```
flask-tic-tac-toe/
├── app.py                  # Main Flask application
├── templates/
│   ├── auth.html          # Database and API authentication
│   ├── index.html         # Main menu and navigation
│   ├── setup.html         # Game configuration page
│   ├── play.html          # Interactive game board
│   └── win_stats.html     # Statistics and performance tracking
├── static/
│   └── style.css          # Custom styling and responsive design
└── README.md             # This file
```

## Requirements

* Python 3.8+
* MySQL server
* Google Gemini API key
* Required packages:
  - Flask
  - mysql-connector-python
  - google-generativeai
  - requests

Install dependencies:

```bash
pip install flask mysql-connector-python google-generativeai requests
```

## Setup

1. Ensure MySQL server is running locally
2. Obtain a Google Gemini API key from Google AI Studio
3. Start the Flask application
4. Configure database credentials and API key through the web interface

## How to Run

Start the Flask development server:

```bash
python app.py
```

Open your browser and navigate to:
```
http://localhost:5000
```

Complete the authentication setup and start playing against the AI.

## How It Works

The Flask application manages game state through session storage, handling player moves and AI responses in real-time. The minimax algorithm evaluates all possible game outcomes to determine the optimal AI move, while the web interface provides immediate visual feedback.

MySQL database stores game results and statistics, allowing players to track their performance across multiple sessions.

## What I Learned

* Flask web framework architecture and routing
* Template rendering with Jinja2 for dynamic content
* Session management for maintaining game state
* Integrating AI algorithms into web applications
* Database operations in web contexts
* Responsive web design with CSS
* Full-stack development workflow from backend to frontend

## Game Difficulty Levels

* **Easy**: AI makes suboptimal moves, allowing player victories
* **Medium**: AI uses limited-depth minimax search
* **Impossible**: Full minimax implementation - unbeatable AI

## Known Issues

* API key and database credentials entered through web form
* Session storage limited to browser session duration
* Basic error handling for database connection issues
* No user authentication or multi-player support
* Limited to single-game sessions

## Possible Improvements

Could add:
* User registration and login system
* Multiplayer online gameplay
* Tournament mode with multiple rounds
* Advanced statistics and analytics dashboard
* Mobile app version using Flask API
* Real-time multiplayer with WebSocket integration
* Different board sizes and game variants

## Author

**Evan William** - Version 2.0 (2025)

Created this web version to learn Flask development and understand how to build interactive web applications. It was great practice for combining AI algorithms with web technologies and creating engaging user interfaces.

This project helped me transition from command-line applications to full web development, focusing on user experience and responsive design.

*Learning project - demonstrates Flask web development and AI algorithm integration in browser-based gaming applications.*
