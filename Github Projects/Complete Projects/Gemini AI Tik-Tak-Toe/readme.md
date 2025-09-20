# AI Tic Tac Toe - Gemini Edition

An advanced Tic Tac Toe game featuring an unbeatable AI opponent powered by the minimax algorithm, with MySQL database integration for game statistics tracking.

## What It Does

This is an intelligent Tic Tac Toe game I built to practice AI algorithms and database integration. The game features three difficulty levels with an AI opponent that uses the minimax algorithm to make optimal moves. On the highest difficulty, the AI is mathematically unbeatable - you can only win or tie.

Built this to learn game AI programming, understand the minimax algorithm, and practice integrating multiple technologies in a single project.

## Features

* Minimax algorithm implementation for perfect AI strategy
* Three difficulty levels: Easy, Medium, and Impossible
* MySQL database integration for persistent game statistics
* Google Gemini API integration for enhanced AI features
* Interactive command-line interface with animated text effects
* User authentication and profile management
* Move validation and game state tracking
* Comprehensive win/loss/tie statistics

## Project Structure

```
ai-tic-tac-toe/
├── main.py              # Main game logic and flow
├── animation.py         # Text animation and visual effects
├── menu.py             # User interface and menu systems
├── authentication.py   # Database setup and user management
├── query_handling.py   # SQL queries and database operations
└── README.md          # This file
```

## Requirements

* Python 3.8+
* MySQL server
* Google Gemini API key
* Required packages:
  - mysql-connector-python
  - inquirer
  - google-generativeai

Install dependencies:

```bash
pip install mysql-connector-python inquirer google-generativeai
```

## Setup

1. Ensure MySQL server is running on your system
2. Obtain a Google Gemini API key from Google AI Studio
3. Run the game and follow setup prompts for database configuration
4. Create a user profile to start tracking statistics

## How to Run

Start the game:

```bash
python main.py
```

Follow the interactive prompts to configure your database connection, set up your profile, and begin playing against the AI.

## How It Works

The game uses the minimax algorithm to evaluate all possible future game states and select the optimal move for the AI. The algorithm recursively explores the game tree, assigning scores to terminal states (win/lose/tie) and propagating these values back up to determine the best current move.

Database integration tracks game outcomes and provides persistent statistics across sessions. The Gemini API integration adds enhanced AI capabilities beyond the core minimax implementation.

## What I Learned

* Minimax algorithm implementation and game tree search
* Recursive programming patterns for AI decision-making
* MySQL database design and query optimization
* API integration with Google's Gemini service
* Game state management and validation logic
* User interface design for command-line applications
* Multi-file Python project organization

## Difficulty Levels

* **Easy**: AI makes random moves with occasional optimal plays
* **Medium**: AI uses minimax but with limited depth search
* **Impossible**: Full minimax implementation - mathematically unbeatable

## Known Issues

* API key must be configured manually on first run
* Database connection requires local MySQL server
* Limited to command-line interface only
* Basic error handling for network issues
* No save/resume game functionality

## Possible Improvements

Could add:
* Web-based interface with HTML/CSS frontend
* Online multiplayer capabilities
* Different board sizes (4x4, 5x5) for variety
* Tournament mode with multiple rounds
* AI personality customization options
* Advanced statistics and performance analytics
* Save game states for resuming later

## Author

**Evan William** - Version 1.0 (2025)

Created this to dive deep into game AI programming and understand how unbeatable game algorithms work. It was excellent practice for combining multiple technologies and building a complete interactive application.

This was my first implementation of the minimax algorithm and helped me understand recursive thinking in AI programming.

*Learning project - demonstrates AI algorithm implementation and multi-technology integration in game development.*
