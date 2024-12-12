import tkinter as tk

from theme import *


class HomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pi-Sync | Home')
        self.configure(bg=BACKGROUND)
        self.geometry('500x300')
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

        frame = tk.Frame(master=self, bg=BACKGROUND)
        hello = tk.Label(
            master=frame,
            text='Hello there, Ralph Maron Eda is here!'
        )
        hello.pack()
        frame.pack(pady=5)

    def on_closing(self):
        self.destroy()
