import customtkinter as ctk


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = ctk.CTkLabel(self, text="Dashboard", font=("Arial", 24))
        label.pack(pady=20)
