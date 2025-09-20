# VTypeC Typing Trainer

A command-line typing trainer application built in C++ with typewriter animations and colorful interface for improving typing speed and accuracy.

## What It Does

This is a terminal-based typing trainer I built to practice C++ programming while creating something useful for improving typing skills. The program displays words with a typewriter animation effect, tracks your typing speed and accuracy, and provides immediate feedback on your performance.

Built this to learn multi-file C++ project organization, cross-platform development, and terminal UI programming with ANSI color codes.

## Features

* Dynamic word generation from 400+ word dictionary
* Real-time typewriter animation effects
* Typing speed calculation (words per second)
* Accuracy tracking with mistake analysis
* Cross-platform screen clearing functionality
* Colorful ANSI terminal interface
* Customizable practice session length
* Mixed vocabulary including programming terms

## Project Structure

```
VTypeC/
├── main.cpp              # Main program logic and menu system
├── clearscreen.cpp       # Cross-platform screen clearing
├── clearscreen.h         # Screen clearing header
├── mistake_counter.cpp   # Speed and accuracy calculations
├── mistake_counter.h     # Mistake tracking header
├── ui.cpp               # Typewriter animation implementation
├── ui.h                 # UI effects header
├── word_generator.cpp   # Random word selection logic
├── word_generator.h     # Word generation header
└── README.md           # This file
```

## Requirements

* C++11 compatible compiler (g++, clang++, MSVC)
* Terminal with ANSI color support
* Standard C++ libraries

## How to Build

Compile all source files together:

**Linux/Mac:**
```bash
g++ -std=c++11 *.cpp -o main
```

**Windows with MinGW:**
```bash
g++ -std=c++11 *.cpp -o main.exe
```

**Manual compilation:**
```bash
g++ -std=c++11 main.cpp clearscreen.cpp mistake_counter.cpp ui.cpp word_generator.cpp -o main
```

## How to Run

Execute the compiled program:

```bash
./main       # Linux/Mac
main.exe     # Windows
```

Choose your practice session length and start typing the words as they appear with the typewriter effect.

## How It Works

The program consists of several modules:
* `main.cpp` handles the overall program flow and user interface
* `word_generator` manages the word dictionary and random selection
* `ui` implements the typewriter animation using ANSI escape sequences
* `mistake_counter` calculates typing statistics and accuracy metrics
* `clearscreen` provides cross-platform terminal clearing functionality

Each word appears with a typewriter animation, and the program tracks your input in real-time to calculate speed and accuracy.

## What I Learned

* Multi-file C++ project organization and header files
* Cross-platform programming techniques
* ANSI escape sequences for terminal colors and effects
* String manipulation and comparison algorithms
* Timing functions for animation and speed calculation
* Memory management with vectors and strings
* Code modularization and separation of concerns

## Known Issues

* ANSI colors may not work on all terminal emulators
* Timing accuracy depends on system timer resolution
* No persistent statistics storage
* Basic word comparison algorithm
* Limited customization options

## Possible Improvements

Could add:
* Persistent user statistics and progress tracking
* Different difficulty levels and word categories
* Configurable animation speed and colors
* Support for custom word lists
* More detailed accuracy analysis
* Leaderboard functionality
* Better cross-platform terminal handling

## Author

**Evan William** - Version 1.0 (2025)

Created this as my first multi-file C++ project to practice object-oriented programming and learn about terminal UI development. It was helpful for understanding how to organize larger C++ programs and work with system-specific functionality.

First time implementing animations in a terminal application, so the code focuses on core functionality while keeping it clean.

*Learning project - demonstrates C++ programming concepts in a practical typing trainer application.*
