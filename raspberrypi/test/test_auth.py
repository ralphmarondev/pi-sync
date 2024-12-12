import tkinter as tk

from src.theme import *
from test_home import HomeWindow


class AuthWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pi-Sync')
        self.configure(bg='#333333')
        self.geometry('500x300')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        frame = tk.Frame(master=self, bg=BACKGROUND)
        login_label = tk.Label(
            master=frame,
            text='Login',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT_DEFAULT
        )
        username_entry = tk.Entry(
            master=frame,
            font=FONT_DEFAULT
        )
        password_entry = tk.Entry(
            master=frame,
            font=FONT_DEFAULT,
            show='*'
        )
        login_btn = tk.Button(
            master=frame,
            text='LOGIN',
            font=('monospace', 14),
            fg=FOREGROUND,
            bg='#FF3399',
            command=lambda: self.handle_login(username_entry, password_entry)
        )

        login_label.grid(row=0, column=0)
        username_entry.grid(row=1, column=0, pady=5)
        password_entry.grid(row=2, column=0, pady=5)
        login_btn.grid(row=3, column=0, pady=5)

        frame.pack(pady=5)

    def handle_login(self, username_entry: tk.Entry, password_entry: tk.Entry):
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        is_success = username == 'ralphmaron' and password == 'iscute'
        if is_success:
            self.destroy()  # Close the authentication window
            HomeWindow().mainloop()  # Open the home window

    def on_closing(self):
        self.destroy()
