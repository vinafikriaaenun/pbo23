import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MP3PlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Vina Pikria Aenun MP3 Player")
        self.master.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="MP3 Player", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.btn_browse = tk.Button(self.master, text="Browse", command=self.browse_file)
        self.btn_browse.pack(pady=10)

        self.btn_play = tk.Button(self.master, text="Play", command=self.play_music)
        self.btn_play.pack(pady=10)

        self.btn_stop = tk.Button(self.master, text="Stop", command=self.stop_music)
        self.btn_stop.pack(pady=10)

        self.file_path = ""

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])

    def play_music(self):
        if self.file_path:
            pygame.mixer.init()
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MP3PlayerApp(root)
    root.mainloop()