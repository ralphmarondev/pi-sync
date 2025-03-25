import tkinter as tk
from tkinter import ttk

from numpy.random import choice

from tenant.new_tenant_dialog import NewTenantDialog

class TenantScreen:
	def __init__(self, parent_frame):
		self.root = parent_frame
		self.table = None

	def content(self):
		first_names = ['Ralph Maron', 'Triesha Mae', 'Jezlyn', 'Jack']
		last_names = ['Eda', 'Olunan', 'Cabbab', 'Cabigayan']

		dashboard_frame = tk.Frame(
			master=self.root,
			highlightbackground='purple',
			highlightthickness=2
		)

		# === Top Frame (Search Bar & Buttons) ===
		top_frame = tk.Frame(dashboard_frame, padx=5, pady=5)
		top_frame.pack(fill="x")

		# Search Field & Search Button
		search_entry = tk.Entry(top_frame, width=30)
		search_entry.pack(side="left", padx=5)

		search_button = tk.Button(top_frame, text="Search", bg="gray", fg="white", command=self.search_action)
		search_button.pack(side="left", padx=5)

		# Right-aligned buttons
		button_frame = tk.Frame(top_frame)  # Wrapper frame to push buttons to the right
		button_frame.pack(side="right")

		all_button = tk.Button(button_frame, text="All", bg="orange", fg="white", command=self.all_action)
		all_button.pack(side="left", padx=5)

		room_button = tk.Button(button_frame, text="Room", bg="blue", fg="white", command=self.room_action)
		room_button.pack(side="left", padx=5)

		new_button = tk.Button(button_frame, text="New", bg="green", fg="white", command=self.new_action)
		new_button.pack(side="left", padx=5)

		# tree view
		columns = ('first', 'last', 'email', 'actions')
		self.table = ttk.Treeview(dashboard_frame, columns=columns, show='headings')

		self.table.heading('first', text='First name')
		self.table.heading('last', text='Last name')
		self.table.heading('email', text='Email')
		self.table.heading('actions', text='Actions')  # Actions Column

		self.table.column('first', width=150)
		self.table.column('last', width=150)
		self.table.column('email', width=200)
		self.table.column('actions', width=80, anchor="center")  # Fixed width for Actions column

		self.table.pack(fill='both', expand=True, padx=5, pady=5)

		# Insert values into the table
		for _ in range(20):
			first = choice(first_names)
			last = choice(last_names)
			email = f'{first.lower()}{last.lower()}@gmail.com'.replace(' ', '')

			# Insert row into table
			row_id = self.table.insert('', 'end', values=(first, last, email, "..."))

		# Bind the treeview to capture clicks on the Actions column
		self.table.bind('<ButtonRelease-1>', self.handle_click)

		return dashboard_frame

	def handle_click(self, event):
		""" Show details when a row is clicked. """
		region = self.table.identify_region(event.x, event.y)
		if region == "cell":
			row_id = self.table.identify_row(event.y)
			col = self.table.identify_column(event.x)

			# Check if the click is in the Actions column
			if col == '#4':  # The "Actions" column
				values = self.table.item(row_id, "values")
				if values:
					first, last, email, _ = values
					self.show_action_menu(event, first, last, email)

	def show_action_menu(self, event, first, last, email):
		""" Display an action menu when clicking the 'Actions' column. """
		menu = tk.Menu(self.root, tearoff=0)
		menu.add_command(label="View Details", command=lambda: self.show_details(first, last, email))
		menu.add_command(label="Update Details", command=lambda: self.update_details(first, last, email))
		menu.add_command(label="Delete Details", command=lambda: self.delete_details(first, last, email))
		menu.post(event.x_root, event.y_root)

	def show_details(self, first, last, email):
		""" Print row details when 'View Details' is clicked. """
		print(f"Viewing details for: {first} {last} - {email}")

	def update_details(self, first, last, email):
		""" Simulate updating details when 'Update Details' is clicked. """
		print(f"Updating details for: {first} {last} - {email}")
		# In a real application, you would prompt the user for new details and update the database.

	def delete_details(self, first, last, email):
		""" Simulate deleting details when 'Delete Details' is clicked. """
		print(f"Deleting details for: {first} {last} - {email}")
		# In a real application, this would delete the row from the table/database.
		# For now, we'll just remove the item from the table.
		for item in self.table.get_children():
			values = self.table.item(item, "values")
			if values and values[0] == first and values[1] == last:
				self.table.delete(item)
				print(f"Deleted {first} {last}")
				break

	def new_action(self):
		# print("New button clicked!")
		dialog = NewTenantDialog(self.root)
		dialog.grab_set() # block interaction from main window

	def room_action(self):
		print("Room button clicked!")

	def all_action(self):
		print("All button clicked!")

	def search_action(self):
		print("Search button clicked!")

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('600x400')

	content_frame = tk.Frame()
	room = TenantScreen(content_frame)
	frame = room.content()

	frame.pack(fill=tk.BOTH, expand=True)
	content_frame.pack(fill=tk.BOTH, expand=True)
	root.mainloop()
