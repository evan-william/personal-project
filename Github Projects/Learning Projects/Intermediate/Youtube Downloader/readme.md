# 🎥 Evan's YouTube Downloader 🎥

## 🚀 Overview

Evan's YouTube Downloader is a friendly command-line tool built with Python, `yt_dlp`, and `inquirer`. It lets you easily download YouTube videos or extract audio in MP3 format with a clean, colorful interface and useful options like resolution selection for videos.

Perfect for quickly grabbing your favorite content directly to your computer with minimal hassle! 💻✨

---

## 🔥 Features

* 🎬 **Video Download**: Choose your preferred video resolution before downloading
* 🎵 **Audio Download**: Extract audio and save as MP3
* 🎨 **Colorful CLI**: Nice colored ASCII art and prompts using `colorama`
* 📂 **Custom Download Folder**: Specify where to save your files
* 🛑 **Exit Option**: Clean exit from the program
* 🤖 **Smart Format Filtering**: Only valid video+audio formats are listed for video downloads

---

## 📋 Requirements

* Python 3.x
* [yt\_dlp](https://github.com/yt-dlp/yt-dlp) (for video/audio downloading)
* [inquirer](https://github.com/magmax/python-inquirer) (for CLI menus)
* [colorama](https://pypi.org/project/colorama/) (for colored terminal output)

Install dependencies with:

```bash
pip install yt_dlp inquirer colorama
```

---

## 💻 How to Use

1. Run the script:

   ```bash
   python your_script_name.py
   ```

2. Choose what to download:

   * 📺 Video (choose resolution)
   * 🎵 Audio (MP3)
   * ❌ Exit

3. Enter the YouTube URL when prompted.

4. Specify the download folder or press Enter to use the current directory.

5. For video downloads, select your desired resolution from the list.

6. Wait for the download to complete.

7. Press Enter to return to the main menu or exit.

---

## 🎨 How It Works

* The script shows a colorful ASCII art banner and a user-friendly menu.
* Uses `yt_dlp` to fetch available video formats and download media.
* Filters video formats to only show those with both audio and video for download.
* Audio downloads grab the best available audio stream and save it as MP3.
* Uses `inquirer` for neat, interactive CLI menus.
* Colored output powered by `colorama` for a fun terminal experience!

---

## 🚧 Future Improvements

* Add progress bar for downloads
* Support playlist downloads
* Add pause/resume functionality
* Option to download subtitles
* Support other platforms beyond YouTube

---

## 👨‍💻 Developer  
Created by Evan William (2025)  
Version: 1.0

