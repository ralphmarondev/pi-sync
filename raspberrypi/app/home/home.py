import tkinter as tk

BACKGROUND = "#f5f5f5"
NAVBAR_COLOR = "#c3c3c3"
ACTIVE_COLOR = "#158aff"
INACTIVE_COLOR = "#c3c3c3"

class HomeScreen(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Pi-Sync | Home')
		self.configure(bg=BACKGROUND)
		self.geometry('800x600')
		self.protocol('WM_DELETE_WINDOW', self.on_closing)

		self.content_frame = None
		self.about_button = None
		self.users_button = None
		self.dashboard_button = None
		self.main_frame = None
		self.rooms_button = None
		self.active_indicator = None

		self.create_widgets()
		self.after(100, self.set_default_active_button)

	def set_default_active_button(self):
		self.set_active_button(self.dashboard_button)

	def on_closing(self):
		self.destroy()

	def create_widgets(self):
		self.main_frame = tk.Frame(self, bg=BACKGROUND)
		self.main_frame.pack(fill=tk.BOTH, expand=True)

		self.navigation_bar(self.main_frame)
		self.content_with_top_bar(self.main_frame)

	def navigation_bar(self, parent):
		navigation_frame = tk.Frame(parent, bg=NAVBAR_COLOR)
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

		self.dashboard_button = self.create_nav_button(navigation_frame, 'Dashboard', self.show_dashboard)
		self.rooms_button = self.create_nav_button(navigation_frame, 'Rooms', self.show_rooms)
		self.users_button = self.create_nav_button(navigation_frame, 'Users', self.show_users)
		self.about_button = self.create_nav_button(navigation_frame, 'About', self.show_about)

	def create_nav_button(self, parent, text, command):
		button = tk.Button(
			master=parent,
			text=text,
			font=('Bold', 16),
			fg=ACTIVE_COLOR,
			bd=0,
			bg=NAVBAR_COLOR,
			anchor='w',
			padx=15,
			pady=5,
			command=command
		)
		button.pack(fill=tk.X, pady=5)
		return button

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

		self.content_frame = tk.Frame(content_wrapper, bg='#ffffff')
		self.content_frame.pack(fill=tk.BOTH, expand=True)
		self.content_frame.pack_propagate(False)

	def show_dashboard(self):
		self.update_content("Dashboard Content")
		self.set_active_button(self.dashboard_button)

	def show_rooms(self):
		self.update_content("Rooms Content")
		self.set_active_button(self.rooms_button)

	def show_users(self):
		self.update_content("Users Content")
		self.set_active_button(self.users_button)

	def show_about(self):
		self.update_content("About Content")
		self.set_active_button(self.about_button)

	def set_active_button(self, button):
		# Remove the previous indicator
		if self.active_indicator:
			self.active_indicator.place_forget()

		self.active_indicator = tk.Label(
			button.master,
			text='',
			bg=ACTIVE_COLOR
		)
		self.active_indicator.place(x=0, y=button.winfo_y(), width=5, height=button.winfo_height())

	def update_content(self, text):
		# Clear existing widgets in the content frame
		for widget in self.content_frame.winfo_children():
			widget.destroy()

		content_label = tk.Label(
			self.content_frame,
			text=text,
			font=('monospace', 24),
			bg='#ffffff'
		)
		content_label.pack(expand=True)

if __name__ == '__main__':
	home = HomeScreen()
	home.mainloop()
