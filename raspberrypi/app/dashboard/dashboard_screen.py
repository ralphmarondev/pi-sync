import tkinter as tk

class DashboardScreen:
	def __init__(self, parent_frame):
		self.root = parent_frame

	def content(self):
		dashboard_frame = tk.Frame(self.root)
		lb = tk.Label(
			master=dashboard_frame,
			text='Dashboard',
			font=('Bold', 30)
		)
		lb.pack()
		return dashboard_frame
