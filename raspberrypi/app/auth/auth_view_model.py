class AuthViewModel:
    def __init__(self):
        self.username = ''
        self.password = ''

    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: str):
        self.password = password

    def login(self):
        # for testing [no need to enter some credentials]
        return True, 'Login successful!'

        if not self.username.strip() or not self.password.strip():
            return False, 'Username or password cannot be empty!'

        # for testing
        if self.username.strip() == 'ralphmaron' and self.password.strip() == 'iscute':
            return True, 'Login successful!'
        return False, 'Login failed! Incorrect credentials.'

        # try:
        #     response = requests.post(
        #         url=f'{API_BASE_URL}login/',
        #         data={'username': self.username, 'password': self.password}
        #     )
        #     if response.status_code == 200:
        #         print(f'Login successful:', response.json())
        #         return True, None
        #     else:
        #         try:
        #             error_message = response.json().get('message', 'Login failed')
        #         except ValueError:
        #             error_message = 'Login failed with unexpected response'
        #         print('Login failed:', response.status_code, error_message)
        #         return False, error_message
        # except requests.RequestException as e:
        #     message = f'Error connecting to the server: {e}'
        #     print(message)
        #     return False, message
