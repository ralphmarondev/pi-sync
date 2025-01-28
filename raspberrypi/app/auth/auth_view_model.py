import requests

from app.constants import API_BASE_URL

class AuthViewModel:
	def __init__(self):
		self.username = ''
		self.password = ''

	def set_username(self, username: str):
		self.username = username

	def set_password(self, password: str):
		self.password = password

	def login(self):
		if not self.username.strip() or not self.password.strip():
			return False, 'Username or password cannot be empty!'

		try:
			response = requests.post(
				url=f'{API_BASE_URL}login/',
				data={'username': self.username, 'password': self.password}
			)
			if response.status_code == 200:
				print(f'Login successful:', response.json())
				return True, None
			else:
				print('Login failed:', response.status_code, response.text)
				return False, response.text
		except requests.RequestException as e:
			message = f'Error connecting to the server: {e}'
			print(message)
			return False, message