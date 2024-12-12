import tkinter as tk

from auth import AuthScreen
from src.home import HomeScreen
from theme import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pi-Sync')
        self.configure(bg=BACKGROUND)
        self.geometry('500x300')

        self.current_frame = None
        self.auth_screen = AuthScreen(self)
        self.home_screen = HomeScreen(self)

        # self.auth_screen.login()
        self.show_frame(self.auth_screen)  # default [auth]

    def show_frame(self, frame):
        if self.current_frame is not None:
            self.current_frame.pack_forget()  # hide prev frame
        self.current_frame = frame
        frame.pack(fill='both', expand=True)


if __name__ == '__main__':
    root = App()

    root.mainloop()
