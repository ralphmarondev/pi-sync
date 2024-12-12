import tkinter as tk

from auth import AuthScreen

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # hide root window

    auth_screen = AuthScreen()
    auth_screen.mainloop()
