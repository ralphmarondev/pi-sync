import tkinter as tk

from app.theme import *

class HomeScreen(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Pi-Sync | Home')
		self.configure(bg=BACKGROUND)
		self.geometry('800x600')
		self.protocol('WM_DELETE_WINDOW', self.on_closing)

		self.main_frame()

	def on_closing(self):
		self.destroy()

	def main_frame(self):
		main_frame = tk.Frame(self, bg=BACKGROUND)
		main_frame.pack(fill=tk.BOTH, expand=True)

		self.navigation_bar(main_frame)
		self.content_with_top_bar(main_frame)

	def navigation_bar(self, parent):
		navigation_frame = tk.Frame(parent, bg='#c3c3c3')
		navigation_frame.pack(side=tk.LEFT, fill=tk.Y)
		navigation_frame.pack_propagate(False)
		navigation_frame.configure(width=200)

		thesis_label = tk.Label(
			master=navigation_frame,
			text='Thesis',
			fg='#ffffff',
			bg='#5E3B8E',
			font=('monospace', 12),
			anchor='center'
		)
		thesis_label.pack(fill=tk.X, side=tk.TOP, ipady=15)

	def content_with_top_bar(self, parent):
		content_wrapper = tk.Frame(parent, bg=BACKGROUND)
		content_wrapper.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

		top_bar = tk.Frame(
			master=content_wrapper,
			bg='#5E3B8E',
			height=40
		)
		top_bar.pack(fill=tk.X, side=tk.TOP)

		user_label = tk.Label(
			master=top_bar,
			text='Ralph Maron Eda',
			fg='#ffffff',
			bg='#5E3B8E',
			font=('monospace', 12),
			anchor='e'
		)
		user_label.pack(side=tk.RIGHT, padx=10, pady=15)

		content_frame = tk.Frame(content_wrapper, bg='#ffffff')
		content_frame.pack(fill=tk.BOTH, expand=True)
		content_frame.pack_propagate(False)

if __name__ == '__main__':
	home = HomeScreen()
	home.mainloop()
