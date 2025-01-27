import tkinter as tk
from tkinter import messagebox

from app.auth.auth_view_model import AuthViewModel
from app.home.home_screen import HomeScreen
from app.theme import *

class AuthScreen(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Pi-Sync | Auth')
		self.configure(bg='#333333')
		self.geometry('500x300')
		self.protocol("WM_DELETE_WINDOW", self.on_closing)

		self.action = AuthViewModel(self)
		self.login()

	def login(self):
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
		is_success = self.action.on_login(
			username=username_entry,
			password=password_entry
		)
		if is_success:
			messagebox.showinfo('Login successful', 'You have logged in successfully!')
			self.destroy()
			HomeScreen().mainloop()
		else:
			messagebox.showerror('Login failed', 'Please try again later.')

	def on_closing(self):
		self.destroy()

if __name__ == '__main__':
	root = AuthScreen()
	root.mainloop()
