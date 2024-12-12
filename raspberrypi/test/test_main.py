import tkinter as tk

from test_auth import TestAuthWindow


def test_main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    auth_window = TestAuthWindow()
    auth_window.mainloop()


if __name__ == "__main__":
    test_main()
