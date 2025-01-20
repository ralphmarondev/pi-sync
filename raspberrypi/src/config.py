import tkinter as tk


class Config:
    def __init__(self, root: tk.Tk):
        self.root = root

    def set_fullscreen(self):
        self.root.attributes('-fullscreen', True)
        self.root.bind('<F11>', self.toggle_fullscreen)

    def toggle_fullscreen(self, event=None):
        current_state = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not current_state)

BASE_URL = 'http://localhost:8000/api/'
