# 🎮 AI Tic Tac Toe - Flask Gemini Edition

This is an **advanced Tic Tac Toe web application in Flask** featuring an **unbeatable AI opponent** using the minimax algorithm. The AI is smart enough to never lose - you can only win on Easy mode or achieve ties on Impossible!

---

## ✨ What It Does

- Uses **minimax algorithm** for perfect AI strategy that never loses
- **3 difficulty levels**: Easy (beatable), Medium (challenging), Impossible (unbeatable)
- **MySQL database** integration to track your wins and losses
- **Web-based interface** with responsive design and smooth gameplay
- **Smart move validation** and user-friendly web interface
- **Real-time game statistics** displayed in your browser

---

## 🚀 How to Run

### **Prerequisites**
```bash
pip install flask mysql-connector-python google-generativeai requests
```

### **Setup**
1. Make sure you have **MySQL** installed and running
2. Get a **Gemini API key** from Google AI Studio
3. Run the Flask app: `python app.py`
4. Open your browser and go to `http://localhost:5000`
5. Enter your database credentials and Gemini API key
6. Start playing!

### **File Structure**
```
📁 Your Flask Project
├── app.py (main Flask application)
├── templates/
│   ├── auth.html (authentication page)
│   ├── index.html (main menu)
│   ├── setup.html (game setup)
│   ├── play.html (game board)
│   └── win_stats.html (statistics page)
└── static/
    └── style.css (styling)
```

---

## 🌐 Features

✔️ **Web-based gameplay** with intuitive click-to-play interface  
✔️ **Real-time AI moves** with visual feedback  
✔️ **Database integration** successfully tracking game statistics  
✔️ **Unbeatable AI** implemented using minimax algorithm  
✔️ **Responsive design** works on desktop and mobile  
✔️ **Session management** maintains game state between moves  

---

## 🎯 How to Play

1. **Authentication**: Enter your MySQL credentials and Gemini API key
2. **Game Setup**: Choose difficulty level and your symbol (X or O)
3. **Play**: Click on empty cells to make your move
4. **Win Tracking**: View your win/loss statistics anytime
5. **Play Again**: Reset and start new games with different settings

---

## ⚙️ Configuration

The app requires:
- **MySQL database** for game statistics storage
- **Gemini API key** for AI integration (though currently used for authentication only)
- **Flask secret key** (change in production!)

---

## 👨‍💻 Developer

Created by Evan William (2025)  
Version: 2.0 - Flask Web Edition