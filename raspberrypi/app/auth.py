import customtkinter as ctk
from tkinter import messagebox
from home import HomeScreen

class AuthScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Login | PiSync")
        self.root.geometry("350x400")
        # self.root.config(bg="transparent")  # Light purple background for the window

        # Create a card frame
        self.card_frame = ctk.CTkFrame(self.root, width=300, height=350, corner_radius=15, fg_color="transparent")
        self.card_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Header Label
        self.header_label = ctk.CTkLabel(self.card_frame, text="Please Login", font=("Arial", 18, "bold"), text_color="#9b59b6")
        self.header_label.pack(pady=20)

        # Username Label and Entry (Aligned Left)
        self.username_label = ctk.CTkLabel(self.card_frame, text="Username", font=("Arial", 12), text_color="#9b59b6", anchor="w")
        self.username_label.pack(pady=5, anchor="w", padx=10)  # Aligned left with padding
        self.username_entry = ctk.CTkEntry(self.card_frame, font=("Arial", 12), width=220, placeholder_text="Enter your username")
        self.username_entry.pack(pady=5, padx=10)  # Added padding for better spacing

        # Password Label and Entry (Aligned Left)
        self.password_label = ctk.CTkLabel(self.card_frame, text="Password", font=("Arial", 12), text_color="#9b59b6", anchor="w")
        self.password_label.pack(pady=5, anchor="w", padx=10)  # Aligned left with padding
        self.password_entry = ctk.CTkEntry(self.card_frame, font=("Arial", 12), width=220, placeholder_text="Enter your password", show="*")
        self.password_entry.pack(pady=5, padx=10)  # Added padding for better spacing

        # Forgot Password Label (Aligned Right)
        self.forgot_password_label = ctk.CTkLabel(self.card_frame, text="Forgot Password?", font=("Arial", 10, "italic"), text_color="#9b59b6", cursor="hand2")
        self.forgot_password_label.pack(pady=5, anchor="e")  # Aligned to the right (east)

        # Login Button
        self.login_button = ctk.CTkButton(self.card_frame, text="Login", font=("Arial", 12, "bold"), fg_color="#9b59b6", hover_color="#8e44ad", text_color="white", command=self.login_action)
        self.login_button.pack(pady=20, ipadx=20, ipady=10)

    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Add logic for authenticating the user here
        if username == "ralphmaron" and password == "iscute":
            messagebox.showinfo("Login Successful", "Welcome back!")
            root.destroy()
            HomeScreen().mainloop()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

if __name__ == '__main__':
    root = ctk.CTk()
    auth_screen = AuthScreen(root)
    root.mainloop()
