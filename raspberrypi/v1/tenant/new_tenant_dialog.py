import tkinter as tk
from tkinter import ttk
"""
- username
- first name
- last name
- is superuser
- email 
- password
- hint password
- gender
- registered doors [name of door]
"""

class NewTenantDialog(tk.Toplevel):
	def __init__(self, parent):
		super().__init__(parent)
		self.title("Add New Tenant")
		self.geometry("600x300")

		frame = tk.Frame(self)
		frame.pack()

		user_info_frame = tk.LabelFrame(frame, text='User Information')
		user_info_frame.grid(row=0, column=0, padx=20, pady=20)

		first_name_label = tk.Label(user_info_frame, text='First Name')
		first_name_label.grid(row=0, column=0)
		last_name_label = tk.Label(user_info_frame, text='Last Name')
		last_name_label.grid(row=0, column=1)

		first_name_entry = tk.Entry(user_info_frame)
		last_name_entry = tk.Entry(user_info_frame)

		first_name_entry.grid(row=1, column=0)
		last_name_entry.grid(row=1, column=1)

		title_label = tk.Label(user_info_frame, text='Title')
		title_combobox = ttk.Combobox(user_info_frame, values=['', 'Mr.', 'Ms.', 'Dr.'])
		title_label.grid(row=0, column=2)
		title_combobox.grid(row=1, column=2)

		for widget in frame.winfo_children():
			widget.grid_configure(padx=10, pady=5)
