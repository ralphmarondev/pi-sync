import tkinter as tk

from app.theme import *

class HomeScreen(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Pi-Sync | Home')
		self.configure(bg=BACKGROUND)
		self.geometry('800x600')
		self.protocol('WM_DELETE_WINDOW', self.on_closing)

		self.top_app_bar()
		self.main_frame()

	def on_closing(self):
		self.destroy()

	def top_app_bar(self):
		top_bar = tk.Frame(
			master=self,
			bg="#5E3B8E",
			height=40
		)
		top_bar.pack(fill=tk.X, side=tk.TOP)
		header_label = tk.Label(
			master=top_bar,
			text="Thesis",
			fg="#ffffff",
			bg='#5E3B8E',
			font=('monospace', 16)
		)
		header_label.pack(padx=10, pady=15)

	def main_frame(self):
		main_frame = tk.Frame(self)
		main_frame.pack(fill=tk.BOTH, expand=True)

		self.navigation_bar(main_frame)
		self.content(main_frame)

	def navigation_bar(self, parent):
		navigation_frame = tk.Frame(parent, bg='#c3c3c3')
		navigation_frame.pack(side=tk.LEFT, fill=tk.Y)
		navigation_frame.pack_propagate(False)
		navigation_frame.configure(width=200)

	def content(self, parent):
		content_frame = tk.Frame(parent, bg='purple')
		content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		content_frame.pack_propagate(False)

if __name__ == '__main__':
	home = HomeScreen()
	home.mainloop()
