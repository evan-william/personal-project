# Evan's YouTube Downloader

A command-line YouTube video and audio downloader built with Python, featuring an interactive interface for selecting download formats and quality options.

## What It Does

This is a YouTube downloader tool I built to practice working with external APIs and command-line interfaces. The program lets users download YouTube videos in various resolutions or extract audio as MP3 files through a colorful, menu-driven interface.

Built this to learn how to integrate third-party libraries like yt-dlp, create interactive CLI applications, and handle file downloads with progress feedback.

## Features

* Download YouTube videos with resolution selection
* Extract audio and convert to MP3 format  
* Interactive command-line menus with colorful interface
* Custom download folder specification
* Smart format filtering for video+audio combinations
* ASCII art banner and colored terminal output
* Clean error handling and user feedback

## Project Structure

```
youtube-downloader/
├── downloader.py       # Main application script
└── README.md          # This file
```

## Requirements

* Python 3.x
* Required packages:
  - yt-dlp (YouTube download functionality)
  - inquirer (interactive CLI menus)
  - colorama (colored terminal output)

Install dependencies:

```bash
pip install yt_dlp inquirer colorama
```

## How to Run

Execute the downloader script:

```bash
python downloader.py
```

Follow the interactive prompts to:
1. Choose between video or audio download
2. Enter the YouTube URL
3. Specify download location
4. Select video resolution (for video downloads)
5. Wait for download completion

## How It Works

The application uses yt-dlp to interface with YouTube's API and fetch available video formats. It presents filtered options through inquirer's interactive menus, allowing users to select their preferred quality before downloading. Audio downloads automatically extract the best available audio stream and convert to MP3.

The colorama library provides terminal colors for a more engaging user experience with ASCII art and colored status messages.

## What I Learned

* Working with external Python libraries and APIs
* Creating interactive command-line interfaces
* File handling and download progress management
* Error handling for network operations
* Terminal styling and user experience design
* Format filtering and media processing concepts
* Menu-driven application architecture

## Known Issues

* No download progress bar implementation
* Limited to single video downloads (no playlists)
* Basic error handling for invalid URLs
* Depends on yt-dlp's YouTube compatibility
* No pause/resume download functionality

## Possible Improvements

Could add:
* Real-time download progress indicators
* Batch playlist download support
* Subtitle download options
* Support for other video platforms
* Download history and resume capabilities
* Configuration file for default settings
* GUI version with tkinter or PyQt

## Author

**Evan William** - Version 1.0 (2025)

Created this to learn how to build practical command-line tools that interact with web services. It was good practice for handling user input, managing downloads, and creating polished CLI experiences.

This was my first project working with video download libraries and interactive terminal interfaces.

*Learning project - demonstrates CLI application development and third-party API integration for media downloads.*
