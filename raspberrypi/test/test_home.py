import tkinter as tk


class HomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pi-Sync - Home')
        self.configure(bg='#333333')
        self.geometry('500x300')
