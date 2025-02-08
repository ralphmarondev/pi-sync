import tkinter as tk

class AboutScreen:
	def __init__(self, parent_frame):
		self.root = parent_frame

	def content(self):
		dashboard_frame = tk.Frame(self.root)
		lb = tk.Label(
			master=dashboard_frame,
			text='Members:',
			font=('Bold', 30)
		)
		lb.pack(pady=5)

		members = [
			'Ralph Maron Eda',
			'Jack Cabigayan',
			'Triesha Mae Olunan',
			'Jezlyn Cabbab'
		]
		for i in range(len(members)):
			lb = tk.Label(
				master = dashboard_frame,
				text=members[i],
				font=('monospace', 20)
			)
			lb.pack()

		adviser_lbl = tk.Label(
			master=dashboard_frame,
			text='Adviser:',
			font=('Bold', 30)
		)
		adviser_lbl.pack(pady=5)
		lb = tk.Label(
			master=dashboard_frame,
			text='Engr. Jerome Paul Viador',
			font=('monospace', 20)
		)
		lb.pack()

		return dashboard_frame
