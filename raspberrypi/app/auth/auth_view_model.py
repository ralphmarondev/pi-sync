import tkinter as tk

import requests

from app.constants import API_BASE_URL

class AuthViewModel:
	def __init__(self, root: tk.Tk):
		self.root = root

	def on_login(self, username: tk.Entry, password: tk.Entry):
		username = username.get()
		password = password.get()
		print(f'Username: {username}, password: {password}')

		try:
			response = requests.post(
				url=f'{API_BASE_URL}login/',
				data={'username': username, 'password': password}
			)
			if response.status_code == 200:
				print(f'Login successful:', response.json())
				return True
			else:
				print('Login failed:', response.status_code, response.text)
				return False
		except requests.RequestException as e:
			print(f'Error connecting to the server: {e}')
			return False
