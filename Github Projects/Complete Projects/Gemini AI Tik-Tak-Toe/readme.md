# 🎮 AI Tic Tac Toe - Ultra Smart Edition

This is an **advanced Tic Tac Toe game in Python** featuring an **unbeatable AI opponent** powered by the **minimax algorithm**. Challenge yourself against three difficulty levels, from beatable to mathematically impossible!

---

## ✨ What It Does

- **🧠 Ultra Smart AI**: Uses minimax algorithm for perfect strategic play
- **⚙️ 3 Difficulty Levels**: Easy, Medium, and Impossible modes
- **📊 Win Tracking**: MySQL database integration to track your victories
- **🎨 Beautiful UI**: Animated text effects and colorful console interface
- **🤖 Gemini AI Integration**: Advanced AI setup with Google's Gemini model
- **💾 Persistent Stats**: Your win/loss records are saved forever

---

## 🎯 Game Features

### **Difficulty Modes**
- **🟢 Easy**: AI makes occasional mistakes (30% random moves) - *You can win!*
- **🟡 Medium**: AI plays smart but not perfect (10% random moves) - *Challenging but fair*
- **🔴 Impossible**: Perfect minimax algorithm - *You can only tie or lose!*

### **Smart AI Strategy**
- **Win Detection**: AI always takes winning moves when available
- **Block Prevention**: AI blocks your winning moves automatically  
- **Optimal Positioning**: Chooses strategically important squares (center, corners)
- **Perfect Calculation**: Evaluates every possible game outcome before moving

### **Database Features**
- Automatic MySQL database setup (`ai_tik_tak_toe`)
- Real-time win/loss tracking
- Detailed statistics with win percentages
- Motivational feedback based on your performance

---

## 🚀 How to Run

### **Prerequisites**
```bash
pip install mysql-connector-python
pip install inquirer
pip install google-generativeai
```

### **Setup Steps**
1. **Clone/Download** the project files
2. **Prepare MySQL** database (will auto-create if needed)
3. **Get Gemini API key** from Google AI Studio
4. **Run the game**:
   ```bash
   python main.py
   ```
5. **Follow the setup prompts** for database and AI configuration

### **Required Files Structure**
```
📁 Project Root
├── 📄 main.py (main game file)
├── 📄 animation.py (text effects)
├── 📄 menu.py (menu display)
├── 📄 authentication.py (database auth)
├── 📄 query_handling.py (SQL queries)
└── 📄 README.md
```

---

## 🎮 How to Play

1. **Choose Difficulty**: Select Easy, Medium, or Impossible
2. **Pick Your Symbol**: X or O (X always goes first)
3. **Make Your Move**: Enter numbers 1-9 for board positions
4. **Watch AI Think**: See the AI calculate the perfect move
5. **Try to Win**: Good luck beating the impossible mode! 😈

### **Board Layout**
```
1 | 2 | 3
4 | 5 | 6  
7 | 8 | 9
```

---

## 🏆 Challenge Yourself

### **Can You Beat The AI?**
- **Easy Mode**: ✅ Definitely winnable
- **Medium Mode**: 🎯 Requires skill and strategy  
- **Impossible Mode**: 🔥 **MATHEMATICALLY UNBEATABLE**

> **Pro Tip**: Even achieving a tie against Impossible mode is considered a victory!

---

## 🛠️ Technical Features

### **Advanced AI Implementation**
- **Minimax Algorithm**: Recursive game tree evaluation
- **Alpha-Beta Pruning**: Optimized for faster calculations
- **Depth-Based Scoring**: Prefers faster wins and slower losses
- **Perfect Strategy**: Never makes suboptimal moves in Impossible mode

### **Database Integration**
- **MySQL Connection**: Secure database authentication
- **Auto Table Creation**: Sets up required tables automatically
- **Win Statistics**: Tracks every game result
- **Performance Analytics**: Win rate calculations and motivational feedback

### **User Experience**
- **Animated Text Effects**: Smooth typing animations
- **Color-Coded Feedback**: Visual success/error indicators
- **Interactive Menus**: Easy navigation with arrow keys
- **Smart Input Validation**: Prevents invalid moves

---

## ⚠️ Notes

This is a **complete, production-ready game** featuring:
- **Professional code structure** with modular file organization
- **Robust error handling** for database and AI connections
- **Advanced game theory implementation** (minimax algorithm)
- **Real-world database integration** with MySQL
- **Modern Python best practices** and clean code principles

The **Impossible difficulty** uses a mathematically perfect algorithm - it's **literally impossible to beat**, only tie!

---

## ✅ Status

✔️ **Fully functional** with all features working  
✔️ **Database integration** tested and stable  
✔️ **AI algorithm** implementing perfect minimax strategy  
✔️ **Three difficulty levels** from beginner to unbeatable  
✔️ **Complete game loop** with statistics tracking  
✔️ **Production-ready code** with proper error handling  

---

## 🎓 What You'll Learn

Playing this game demonstrates:
- **Game Theory**: Understanding optimal strategy
- **Algorithm Complexity**: How minimax evaluates millions of possibilities
- **Database Design**: Real-world data persistence
- **Python Programming**: Advanced features and best practices
- **AI Concepts**: How computers can achieve "perfect" play

---

## 👨‍💻 Developer

**Created with ❤️ for AI enthusiasts and game lovers**  
**Version**: 2.0 Ultra Smart Edition  
**Language**: Python 3.x  
**AI Algorithm**: Minimax with Alpha-Beta Pruning  

---

### 🎮 **Ready to Challenge the Unbeatable AI?**
*Run the game and see if you can achieve the impossible!*