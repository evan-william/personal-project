# Evan's Music Player

A simple desktop music player built with Python to practice GUI programming and audio handling. Uses Tkinter for the interface and Pygame for playing MP3 files.

## What It Does

This is a basic music player I made to learn how to build desktop applications with Python. It can load MP3 files from folders, create playlists, and play music with standard controls like play, pause, next, etc.

I wanted to practice working with GUI frameworks and audio libraries, so I built something I'd actually use for playing music on my computer.

## Features

- Load MP3 files from folders or add individual songs
- Simple playlist management
- Basic playback controls (play, pause, stop, next)
- Search function to filter songs
- Customizable theme colors
- Custom background images
- Double-click songs to play them

## Requirements

- Python 3.x
- Pygame (for audio)
- Pillow/PIL (for image handling)

Install dependencies:
```bash
pip install pygame pillow
```

## How to Use

Run the script:
```bash
python music_player.py
```

Then:
1. Use File menu to open a folder with MP3s or add individual songs
2. Songs appear in the playlist
3. Use the search bar to filter if you have lots of songs
4. Click a song and hit play, or double-click to play directly
5. Customize the look from the Theme menu

## How It's Built

- Tkinter for the GUI (using a dark theme)
- Pygame for handling MP3 playback
- Listbox widget to show the playlist
- Search filtering updates the display in real-time
- Theme system lets you change colors and backgrounds

## What I Learned

- Building GUI applications with Tkinter
- Working with audio files using Pygame
- File dialogs and folder browsing
- Event handling for user interactions
- Managing application state (current song, playlist, etc.)
- Image processing with PIL for backgrounds

## Current Limitations

- Only supports MP3 files
- No volume control yet
- Can't save/load playlists
- No progress bar or time display
- Pause doesn't remember position (restarts song)

## Things I Want to Add

- Volume slider
- Progress bar showing song position
- Support for more audio formats
- Playlist saving/loading
- Better pause/resume functionality
- Shuffle and repeat modes

## Project Structure

```
music_player.py    # Main application file
```

The app creates its own GUI elements dynamically, so no additional files needed.

## Author

**Evan William**  
Version 1.0 (2025)

Built this to practice desktop application development in Python. It was a good project for learning about GUI programming, file handling, and audio libraries all in one.

The interface is pretty basic but functional. Good starting point for understanding how desktop apps work before moving to more complex frameworks.

---

*Learning project - feel free to modify or improve it.*
