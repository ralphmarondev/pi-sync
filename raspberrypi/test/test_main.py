import tkinter as tk

from test_auth import AuthWindow
from test_home import HomeWindow

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    auth_window = AuthWindow()
    auth_window.mainloop()

if __name__ == "__main__":
    main()