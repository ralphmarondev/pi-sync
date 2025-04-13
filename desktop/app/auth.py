from tkinter import messagebox

import customtkinter as ctk
import requests

from constants import *
from home import HomeScreen


class AuthScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Login | PiSync")
        self.root.geometry("600x400")  # Set window size (this is optional)

        # theme remove this later
        ctk.set_appearance_mode('light')
        # ctk.set_default_color_theme('purple_theme.json')
        ctk.set_default_color_theme('green')

        # Create the outer frame that will hold the inner frames, adjust to maximum width
        self.outer_frame = ctk.CTkFrame(self.root, corner_radius=15, fg_color="transparent")
        self.outer_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Use grid layout to fill space properly
        self.outer_frame.grid_columnconfigure(0, weight=1, uniform="equal")  # Left frame will take 50%
        self.outer_frame.grid_columnconfigure(1, weight=1, uniform="equal")  # Right frame will take 50%
        self.outer_frame.grid_rowconfigure(0, weight=1)  # Vertical stretch for the frames

        # Create the first inner frame (left side)
        self.left_frame = ctk.CTkFrame(self.outer_frame, corner_radius=15, fg_color="transparent")
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Left frame content: Add any content you want to display on the left side (e.g., logo, image, etc.)
        self.logo_label = ctk.CTkLabel(self.left_frame, text="Logo Here", font=("Arial", 16, "bold"),
                                       text_color="#9b59b6")
        self.logo_label.pack(pady=40)

        # Create the second inner frame (right side, where the login form goes)
        self.right_frame = ctk.CTkFrame(self.outer_frame, corner_radius=15, fg_color="#f5f5f5")
        self.right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Header Label
        self.header_label = ctk.CTkLabel(self.right_frame, text="Please Login", font=("Arial", 18, "bold"),
                                         text_color="#9b59b6")
        self.header_label.pack(pady=(30, 20))  # Added padding at the top for better spacing

        # Username Label and Entry (Aligned Left)
        self.username_label = ctk.CTkLabel(self.right_frame, text="Username", font=("Arial", 14), text_color="#9b59b6",
                                           anchor="w")
        self.username_label.pack(pady=(10, 5), anchor="w", padx=20)  # Consistent padding
        self.username_entry = ctk.CTkEntry(self.right_frame, font=("Arial", 14), width=220,
                                           placeholder_text="Enter your username")
        self.username_entry.pack(pady=(5, 15), padx=20)  # Consistent padding

        # Password Label and Entry (Aligned Left)
        self.password_label = ctk.CTkLabel(self.right_frame, text="Password", font=("Arial", 14), text_color="#9b59b6",
                                           anchor="w")
        self.password_label.pack(pady=(5, 5), anchor="w", padx=20)  # Consistent padding
        self.password_entry = ctk.CTkEntry(self.right_frame, font=("Arial", 14), width=220,
                                           placeholder_text="Enter your password", show="*")
        self.password_entry.pack(pady=(5, 20), padx=20)  # Consistent padding

        # Login Button
        self.login_button = ctk.CTkButton(self.right_frame, text="Login", font=("Arial", 12, "bold"),
                                          fg_color="#9b59b6", hover_color="#8e44ad", text_color="white",
                                          command=self.login_action)
        self.login_button.pack(pady=(20, 5), ipadx=20, ipady=10)

        # Forgot Password Label (Centered below the Login Button)
        self.forgot_password_label = ctk.CTkLabel(self.right_frame, text="Forgot Password?",
                                                  font=("Arial", 10, "italic"),
                                                  text_color="#9b59b6", cursor="hand2")
        self.forgot_password_label.pack(pady=5)  # Centered by default

    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Missing info", "Please enter both username and password")
            return

        try:
            url = f'{BASE_URL}login/'
            payload = {
                'username': username,
                'password': password
            }
            response = requests.post(url, json=payload)
            response.raise_for_status()
            result = response.json()

            if result.get('success'):
                messagebox.showinfo("Login successful", result.get('message', 'Welcome back'))
                self.root.destroy()
                HomeScreen().mainloop()
            else:
                messagebox.showerror('Login failed', result.get('message', 'Invalid credentials.'))
        except requests.RequestException as e:
            print(f'Login error: {e}')
            messagebox.showerror('Error', 'Failed to connect to the server.')


if __name__ == '__main__':
    root = ctk.CTk()

    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('purple_theme.json')

    auth_screen = AuthScreen(root)
    root.mainloop()
