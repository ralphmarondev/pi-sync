import tkinter as tk
from auth.auth_view_model import AuthViewModel
from config import Config
from home.home_screen import HomeScreen
from theme import *
from tkinter import messagebox

class AuthScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pi-Sync | Auth')
        self.configure(bg='#333333')
        self.geometry('600x400')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        config = Config(self)
        config.set_fullscreen()
        config.toggle_fullscreen()

        self.view_model = AuthViewModel()
        self.login_ui()

    def login_ui(self):
        frame = tk.Frame(master=self, bg=BACKGROUND)
        login_label = tk.Label(
            master=frame,
            text='Login',
            bg=BACKGROUND,
            fg='#FF3399',
            font=('monospace', 18),
        )

        username_label = tk.Label(
            master=frame,
            text='Username:',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT_LABEL
        )
        username_entry = tk.Entry(
            master=frame,
            font=FONT_DEFAULT
        )

        password_label = tk.Label(
            master=frame,
            text='Password:',
            fg=FOREGROUND,
            bg=BACKGROUND,
            font=FONT_LABEL
        )
        password_entry = tk.Entry(
            master=frame,
            font=FONT_DEFAULT,
            show='*'
        )

        button_width = max(len('LOGIN'), len(username_entry.get()), len(password_entry.get())) * 2
        login_btn = tk.Button(
            master=frame,
            text='LOGIN',
            font=('monospace', 14),
            fg=FOREGROUND,
            bg='#FF3399',
            command=lambda: self.handle_login(username_entry, password_entry),
            width=button_width,
            cursor='hand2'
        )

        forgot_password_label = tk.Label(
            master=frame,
            text='Forgot Password?',
            fg='#ff3399',
            bg=BACKGROUND,
            font=FONT_LABEL,
            cursor='hand2',
            relief='flat',
            underline=True,
            padx=10, pady=10
        )
        forgot_password_label.bind('<Button-1>', self.on_forgot_password)

        login_label.grid(row=0, column=0, pady=(0, 15))
        username_label.grid(row=1, column=0, sticky='w', pady=5)
        username_entry.grid(row=2, column=0, pady=(0, 10))
        password_label.grid(row=3, column=0, sticky='w', pady=5)
        password_entry.grid(row=4, column=0, pady=(0, 10))
        login_btn.grid(row=5, column=0, pady=10)
        forgot_password_label.grid(row=6, column=0, columnspan=2, pady=5)

        frame.pack(pady=10)

    def handle_login(self, username_entry: tk.Entry, password_entry: tk.Entry):
        self.view_model.set_username(username_entry.get())
        self.view_model.set_password(password_entry.get())

        is_success, message = self.view_model.login()

        if is_success:
            messagebox.showinfo('Login successful', 'You have logged in successfully!')
            self.destroy()
            HomeScreen().mainloop()
        else:
            messagebox.showerror(title='Login failed', message=message)

    def on_forgot_password(self, event=None):
        messagebox.showinfo('Forgot Password', 'Sit back, relax and try remembering it again.')

    def on_closing(self):
        self.destroy()

if __name__ == '__main__':
    root = AuthScreen()
    root.mainloop()
