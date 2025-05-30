# 🎵 Evan's Music Player

## Overview

Evan's Music Player is a simple, user-friendly desktop application built with Python’s Tkinter and Pygame libraries. It lets you play your favorite MP3 songs from folders or individual files with a clean interface and customizable theme and background.

The app is designed to be lightweight and easy to use — perfect for managing and enjoying your music collection without unnecessary complexity.

---

## Features

* **Open Folder**: Load all MP3 files from a selected folder into your playlist
* **Add Song**: Add individual MP3 files to your playlist
* **Search**: Quickly filter songs by name using the search bar
* **Play/Pause**: Play selected songs or the first in the list by default
* **Stop**: Stop the current song
* **Next**: Skip to the next song in the playlist (loops back to the start)
* **Customizable Theme Color**: Choose your own color for buttons and highlights
* **Custom Background Image**: Set any image as the app’s background for a personalized look
* **Double-click to Play**: Double-click any song in the list to start playing it immediately

---

## Requirements

* Python 3.x
* [Pygame](https://www.pygame.org/news) (for audio playback)
* [Pillow (PIL)](https://python-pillow.org/) (for image processing)

Install the required packages with:

```bash
pip install pygame pillow
```

---

## How to Use

1. Run the script:

   ```bash
   python music_player.py
   ```
2. Use the **File** menu to open a folder containing MP3 files or add individual songs.
3. Use the search bar at the top to filter your playlist by song name.
4. Select a song and click **Play** or double-click the song in the list to start playback.
5. Use **Stop** to stop playback or **Next** to skip to the next song.
6. Customize the look by choosing **Change Theme Color** and **Change Background** from the **Theme** menu.

---

## Screenshots

*(You can add screenshots here to showcase your app’s UI)*

---

## How It Works

* The app initializes a Tkinter window with a dark theme.
* Pygame’s mixer module handles audio playback.
* Songs are stored in a list with full file paths and displayed by filename in a Listbox.
* The search bar dynamically filters the playlist based on text input.
* Background and theme color are customizable with file dialogs and color pickers.

---

## Future Improvements

* Add pause/resume functionality
* Support for playlists saving/loading
* Display song duration and playback progress
* Volume control slider
* Support other audio formats beyond MP3

---

## Developer

Created by Evan William (2025)
