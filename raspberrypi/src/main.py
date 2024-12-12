import tkinter as tk

from config import Config
from auth import AuthScreen
from theme import *

if __name__ == '__main__':
    root = tk.Tk()
    auth = AuthScreen(root)

    root.title('Pi-Sync')
    root.configure(bg=BACKGROUND)
    root.geometry('500x300')

    config = Config(root)
    config.set_fullscreen()
    config.toggle_fullscreen()

    auth.login()
    root.mainloop()
