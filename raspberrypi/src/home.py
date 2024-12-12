import tkinter as tk

from theme import *


class HomeScreen:
    def __init__(self, root: tk.Tk):
        self.root = root
        frame = tk.Frame(master=self.root, bg=BACKGROUND)
        hello = tk.Label(
            master=frame,
            text='Hello there, Ralph Maron Eda is here!'
        )
        hello.pack()
        frame.pack(pady=5)
