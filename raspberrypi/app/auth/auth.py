import tkinter as tk

import requests

from app.config import BASE_URL
from app.home.home import HomeScreen
from app.theme import *

class AuthScreen(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Pi-Sync | Auth')
		self.configure(bg='#333333')
		self.geometry('500x300')
		self.protocol("WM_DELETE_WINDOW", self.on_closing)

		self.action = AuthScreenAction(self)
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
		# is_success = self.action.on_login(
		# 	username=username_entry,
		# 	password=password_entry
		# )
		is_success = True
		if is_success:
			self.destroy()
			HomeScreen().mainloop()

	def on_closing(self):
		self.destroy()

class AuthScreenAction:
	def __init__(self, root: tk.Tk):
		self.root = root

	def on_login(self, username: tk.Entry, password: tk.Entry):
		username = username.get()
		password = password.get()
		print(f'Username: {username}, password: {password}')

		try:
			response = requests.post(f'{BASE_URL}login/', data={'username': username, 'password': password})
			if response.status_code == 200:
				print(f'Login successful:', response.json())
				return True
			else:
				print('Login failed:', response.status_code, response.text)
				return False
		except requests.RequestException as e:
			print(f'Error connecting to the server: {e}')
			return False

if __name__ == '__main__':
	root = AuthScreen()
	root.mainloop()
