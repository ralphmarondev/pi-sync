import tkinter as tk
from tkinter import ttk

from numpy.random import choice

class RoomScreen:
	def __init__(self, parent_frame):
		self.root = parent_frame

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
		table = ttk.Treeview(dashboard_frame, columns=('first', 'last', 'email'), show='headings')
		table.heading('first', text='First name')
		table.heading('last', text='Last name')
		table.heading('email', text='Email')
		table.pack(fill='both', expand=True, padx=5, pady=5)

		# insert values into a table
		# table.insert(parent='', index = 0, values=('Angel', 'Apay', 'apayangel@gmail.com'))
		for i in range(20):
			first = choice(first_names)
			last = choice(last_names)
			email = f'{first.lower()}{last.lower()}@gmail.com'.replace(' ','')
			data = (first, last, email)
			table.insert(parent='', index=0,values=data)

		table.insert(parent='', index=0, values=('xxxx','yyyy','zzzz'))

		# events
		table.bind('<<TreeviewSelect>>', self.item_select)
		table.bind('<Delete>', self.delete_items)

		return dashboard_frame

	def new_action(self):
		print("New button clicked!")

	def room_action(self):
		print("Room button clicked!")

	def all_action(self):
		print("All button clicked!")

	def search_action(self):
		print("Search button clicked!")

	def item_select(self, event):
		table = event.widget
		for i in table.selection():
			print(table.item(i)['values'])

	def delete_items(self, event):
		table = event.widget
		for i in table.selection():
			table.delete(i)


if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('600x400')

	content_frame = tk.Frame()
	room = RoomScreen(content_frame)
	frame = room.content()

	frame.pack(fill=tk.BOTH, expand=True)
	content_frame.pack(fill=tk.BOTH, expand=True)
	root.mainloop()
