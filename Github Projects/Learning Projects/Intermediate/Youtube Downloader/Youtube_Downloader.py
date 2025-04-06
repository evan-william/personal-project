import yt_dlp
import inquirer
import os
import platform
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    """ Clears the screen based on the OS. """
    os.system("cls" if platform.system() == "Windows" else "clear")

# ASCII Art 
ASCII_ART = f"""
{Fore.RED}███████╗{Fore.YELLOW}██╗   ██╗{Fore.GREEN}███████╗{Fore.CYAN}███╗   ██╗{Fore.MAGENTA}     ██╗   ██╗{Fore.BLUE}████████╗
{Fore.RED}██╔════╝{Fore.YELLOW}██║   ██║{Fore.GREEN}██╔════╝{Fore.CYAN}████╗  ██║{Fore.MAGENTA}     ╚██╗ ██╔╝{Fore.BLUE}╚══██╔══╝
{Fore.RED}█████╗  {Fore.YELLOW}██║   ██║{Fore.GREEN}█████╗  {Fore.CYAN}██╔██╗ ██║{Fore.MAGENTA}█████╗╚████╔╝ {Fore.BLUE}   ██║   
{Fore.RED}██╔══╝  {Fore.YELLOW}╚██╗ ██╔╝{Fore.GREEN}██╔══╝  {Fore.CYAN}██║╚██╗██║{Fore.MAGENTA}╚════╝ ╚██╔╝  {Fore.BLUE}   ██║   
{Fore.RED}███████╗{Fore.YELLOW} ╚████╔╝ {Fore.GREEN}███████╗{Fore.CYAN}██║ ╚████║{Fore.MAGENTA}        ██║   {Fore.BLUE}   ██║   
{Fore.RED}╚══════╝{Fore.YELLOW}  ╚═══╝  {Fore.GREEN}╚══════╝{Fore.CYAN}╚═╝  ╚═══╝{Fore.MAGENTA}        ╚═╝   {Fore.BLUE}   ╚═╝  
"""

CREATOR = f"{Fore.LIGHTCYAN_EX}Created by Evan William {Fore.YELLOW}(Version: 1.0)"

def show_main_menu(): 
    clear_screen()
    print(ASCII_ART)
    print(f"{CREATOR.center(80)}\n")
    
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}🎛 What would you like to download?{Style.RESET_ALL}")

    questions = [
        inquirer.List("format", message="Choose an option:", choices=[
            "📺 Video (Choose Resolution)",
            "🎵 Audio (MP3)",
            "❌ Exit"
        ])
    ]
    
    answers = inquirer.prompt(questions)
    return answers["format"]

def get_available_resolutions(url):
    ydl_opts = {"quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get("formats", [])

        # Filter valid video formats
        video_formats = [
            (f"{fmt['height']}p", fmt["format_id"])
            for fmt in formats if fmt.get("vcodec") != "none" and fmt.get("acodec") != "none"
        ]

        # Remove duplicates and sort
        video_formats = sorted(set(video_formats), key=lambda x: int(x[0][:-1]))

        return video_formats

def download_video(url, folder="."):
    clear_screen()
    print("🎬 Fetching available resolutions...\n")

    resolutions = get_available_resolutions(url)

    if not resolutions:
        print("❌ No valid video formats found!")
        return

    questions = [inquirer.List("resolution", message="🔽 Choose resolution", choices=resolutions)]
    answer = inquirer.prompt(questions)

    selected_format = answer["resolution"]

    ydl_opts = {
        "format": selected_format,
        "outtmpl": f"{folder}/%(title)s.%(ext)s"
    }

    print(f"\n🎬 Downloading video at {selected_format}...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("✅ Video download complete!")

def download_audio(url, folder="."):
    """ Downloads audio as MP3. """
    clear_screen()
    print("🎵 Preparing to download audio...\n")

    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": f"{folder}/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("✅ Audio download complete!")

if __name__ == "__main__":
    while True:
        choice = show_main_menu()

        if choice == "❌ Exit":
            clear_screen()
            print("👋 Goodbye!")
            break

        url = input("\n🎬 Enter YouTube Video URL: ")
        folder = input("📂 Enter download folder (or press Enter for current directory): ").strip() or "."

        if choice == "📺 Video (Choose Resolution)":
            download_video(url, folder)
        elif choice == "🎵 Audio (MP3)":
            download_audio(url, folder)

        input("\n🔄 Press Enter to return to the main menu...")
        

