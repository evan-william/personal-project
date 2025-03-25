import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
import pygame
import os

def init_app():
    global root, song_list, current_song, theme_color, bg_label, search_var, search_entry, listbox, btn_frame, play_btn, stop_btn, next_btn
    
    root = tk.Tk()
    root.title("Evan's Music Player")
    root.geometry("700x500")
    root.configure(bg="#1e1e1e")
    
    pygame.mixer.init()
    song_list = []
    current_song = None
    theme_color = "#4CAF50"  
    
    bg_label = tk.Label(root)
    bg_label.place(relwidth=1, relheight=1)
    load_background()
    
    search_var = tk.StringVar()
    search_entry = tk.Entry(root, textvariable=search_var, font=("Arial", 14), bg="#333", fg="white", bd=0)
    search_entry.pack(pady=10, fill=tk.X, padx=20)
    search_entry.bind("<KeyRelease>", search_song)
    
    listbox = tk.Listbox(root, font=("Arial", 12), bg="#282828", fg="white", bd=0, selectbackground=theme_color)
    listbox.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)
    listbox.bind("<Double-Button-1>", play_selected_song)
    
    btn_frame = tk.Frame(root, bg=theme_color)
    btn_frame.pack(pady=10)
    
    play_btn = tk.Button(btn_frame, text="▶ Play", command=play_song, bg=theme_color, fg="white", font=("Arial", 12), padx=20)
    play_btn.grid(row=0, column=0, padx=5)
    
    stop_btn = tk.Button(btn_frame, text="■ Stop", command=stop_song, bg="#f44336", fg="white", font=("Arial", 12), padx=20)
    stop_btn.grid(row=0, column=1, padx=5)
    
    next_btn = tk.Button(btn_frame, text="⏭ Next", command=next_song, bg="#2196F3", fg="white", font=("Arial", 12), padx=20)
    next_btn.grid(row=0, column=2, padx=5)
    
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open Folder", command=open_folder)
    file_menu.add_command(label="Add Song", command=add_song)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)
    
    theme_menu = tk.Menu(menubar, tearoff=0)
    theme_menu.add_command(label="Change Theme Color", command=change_theme)
    theme_menu.add_command(label="Change Background", command=change_background)
    menubar.add_cascade(label="Theme", menu=theme_menu)
    
    root.config(menu=menubar)
    root.mainloop()

def open_folder():
    global song_list
    folder = filedialog.askdirectory()
    if folder:
        song_list = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith(".mp3")]
        update_playlist()

def add_song():
    global song_list
    file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file:
        song_list.append(file)
        update_playlist()

def update_playlist():
    listbox.delete(0, tk.END)
    for song in song_list:
        listbox.insert(tk.END, os.path.basename(song))

def search_song(event):
    query = search_var.get().lower()
    listbox.delete(0, tk.END)
    for song in song_list:
        if query in os.path.basename(song).lower():
            listbox.insert(tk.END, os.path.basename(song))

def play_selected_song(event):
    global current_song
    selected_index = listbox.curselection()
    if selected_index:
        current_song = song_list[selected_index[0]]
        play_song()

def play_song():
    global current_song
    if not song_list:
        messagebox.showerror("Error", "No songs available to play!")
        return
    
    if not current_song:
        current_song = song_list[0] 
    
    try:
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to play song: {str(e)}")

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    if current_song in song_list:
        index = song_list.index(current_song)
        next_index = (index + 1) % len(song_list)
        current_song = song_list[next_index]
        play_song()

def change_theme():
    global theme_color
    new_color = colorchooser.askcolor()[1]
    if new_color:
        theme_color = new_color
        play_btn.config(bg=theme_color)
        stop_btn.config(bg=theme_color)
        next_btn.config(bg=theme_color)
        listbox.config(selectbackground=theme_color)
        btn_frame.config(bg=theme_color)
        root.config(bg=theme_color)

def change_background():
    file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file:
        bg_image = Image.open(file)
        bg_image = bg_image.resize((700, 500), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_label.config(image=bg_image)
        bg_label.image = bg_image

def load_background():
    if os.path.exists("background.jpeg"):
        bg_image = Image.open("background.jpeg")
        bg_image = bg_image.resize((700, 500), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_label.config(image=bg_image)
        bg_label.image = bg_image

init_app() 