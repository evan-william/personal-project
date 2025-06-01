# ⌨️ VTypeC Typing Trainer
### Created by Evan William

---

## 📜 Description

A sleek command-line typing trainer built in C++ that helps you level up your typing speed and accuracy. Features a beautiful ASCII art interface with colorful text and smooth typewriter animations.

Perfect for programmers, students, or anyone who wants to improve their typing skills with a mix of everyday words and tech terminology!

---

## ⚙️ Requirements

- **C++11** or newer compiler (g++, clang++, MSVC)
- Terminal with ANSI color support
- These files need to be compiled together:
  - `main.cpp`
  - `clearscreen.cpp` 
  - `mistake_counter.cpp`
  - `ui.cpp`
  - `word_generator.cpp`

---

## 🔨 How To Build

**On Linux/Mac:**
```bash
g++ -std=c++11 *.cpp -o main
```

**On Windows (with MinGW):**
```bash
g++ -std=c++11 *.cpp -o main.exe
```

**Or compile individually:**
```bash
g++ -std=c++11 main.cpp clearscreen.cpp mistake_counter.cpp ui.cpp word_generator.cpp -o main
```

---

## ▶️ How To Run

1. Compile the program (see above)
2. Run it:
```bash
./main       # Linux/Mac
main.exe      # Windows
```
3. Choose how many words to practice (10-100)
4. Watch the words appear with typewriter effect
5. Type them as fast and accurately as you can!

---

## 🎯 What It Does

- **Dynamic Word Generation** - 400+ words from basic vocabulary to programming terms
- **Real-time Typewriter Animation** - Words appear letter by letter (just like old typewriters!)
- **Accuracy Analysis** - Shows exactly what you typed vs. what was expected
- **Speed Tracking** - Calculates your words per second
- **Cross-Platform** - Works on Windows, Mac, and Linux
- **Colorful Interface** - ANSI colors make everything look awesome

---

## 🧰 Project Structure

```
VTypeC/
├── main.cpp              # Main program logic & UI
├── clearscreen.cpp/.h    # Cross-platform screen clearing
├── mistake_counter.cpp/.h # Accuracy & speed calculations  
├── ui.cpp/.h             # Typewriter animation effects
├── word_generator.cpp/.h  # Random word selection
└── README.md             # You are here!
```

---

## 👍 Cool Features

The **typewriter effect** is the star of the show - words appear character by character with customizable delay, making practice sessions feel engaging rather than boring.

**Smart accuracy tracking** compares word-by-word instead of character-by-character, so small typos don't completely wreck your score.

**Massive word dictionary** includes everything from "cat" and "dog" to "asynchronous" and "multithreading" - perfect for building both general and technical typing skills.

---

## 🧰 If Something Breaks

| Problem | Fix |
|---------|-----|
| Colors don't show | Your terminal might not support ANSI colors |
| Won't compile | Make sure you're using C++11 or newer |
| Screen doesn't clear | Terminal compatibility issue - try different terminal |
| Animation too fast/slow | Modify the delay in `typeText()` function |

---

## 👨‍💻 Developer  
Created by Evan William (2025)  
Version: 1.0
