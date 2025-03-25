import tkinter as tk

from about.about_screen import AboutScreen
from config import Config
from dashboard.dashboard_screen import DashboardScreen
from manual.manual_screen import ManualScreen
from room.room_screen import RoomScreen
from tenant.tenant_screen import TenantScreen
from user.user_screen import UserScreen

BACKGROUND = "#f5f5f5"
NAVBAR_COLOR = "#c3c3c3"
ACTIVE_COLOR = "#FF3399"
INACTIVE_COLOR = "#c3c3c3"

class HomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pi-Sync | Home')
        self.configure(bg=BACKGROUND)
        self.geometry('800x600')
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

        config = Config(self)
        config.set_fullscreen()
        config.toggle_fullscreen()

        self.content_frame = None
        self.about_button = None
        self.users_button = None
        self.dashboard_button = None
        self.main_frame = None
        self.rooms_button = None
        self.tenant_button = None
        self.manual_button = None
        self.active_indicator = None

        # screens
        self.dashboard_screen = None
        self.room_screen = None
        self.tenant_screen = None
        self.user_screen = None
        self.manual_screen = None
        self.about_screen = None

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
            font=('monospace', 14),
            anchor='w',
            padx=5
        )
        thesis_label.pack(fill=tk.X, side=tk.TOP, ipady=16)

        self.dashboard_button = self.create_nav_button(navigation_frame, 'Dashboard', self.update_content, 'dashboard')
        self.rooms_button = self.create_nav_button(navigation_frame, 'Rooms', self.update_content, 'rooms')
        self.tenant_button = self.create_nav_button(navigation_frame, 'Tenants', self.update_content, 'tenants')
        self.users_button = self.create_nav_button(navigation_frame, 'Users', self.update_content, 'users')
        self.manual_button = self.create_nav_button(navigation_frame, 'Manual', self.update_content, 'manual')
        self.about_button = self.create_nav_button(navigation_frame, 'About', self.update_content, 'about')

    def create_nav_button(self, parent, text, command, arg):
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
            command=lambda: command(arg)
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
            font=('monospace', 16),
            anchor='e'
        )
        user_label.pack(side=tk.RIGHT, padx=10, ipady=15)

        self.content_frame = tk.Frame(content_wrapper, bg='#ffffff')
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        self.content_frame.pack_propagate(False)

    def set_active_button(self, button):
        if self.active_indicator:
            self.active_indicator.place_forget()

        self.active_indicator = tk.Label(
            button.master,
            text='',
            bg=ACTIVE_COLOR
        )
        self.active_indicator.place(x=0, y=button.winfo_y(), width=5, height=button.winfo_height())

    def update_content(self, screen_name):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        if screen_name == 'dashboard':
            self.dashboard_screen = DashboardScreen(self.content_frame)
            frame = self.dashboard_screen.content()
            if frame is not None:
                frame.pack(fill=tk.BOTH, expand=True)
                self.set_active_button(self.dashboard_button)
            else:
                print('Error: Dashboard screen content is None')

        elif screen_name == 'rooms':
            self.room_screen = RoomScreen(self.content_frame)
            frame = self.room_screen.content()
            if frame is not None:
                frame.pack(fill=tk.BOTH, expand=True)
                self.set_active_button(self.rooms_button)
            else:
                print('Error: Rooms screen content is None')

        elif screen_name == 'tenants':
            self.tenant_screen = TenantScreen(self.content_frame)
            frame = self.tenant_screen.content()
            if frame is not None:
                frame.pack(fill=tk.BOTH, expand=True)
                self.set_active_button(self.tenant_button)
            else:
                print('Error: Tenant screen content is None')

        elif screen_name == 'users':
            self.user_screen = UserScreen(self.content_frame)
            frame = self.user_screen.content()
            if frame is not None:
                frame.pack(fill=tk.BOTH, expand=True)
                self.set_active_button(self.users_button)
            else:
                print('Error: Users screen content is None')

        elif screen_name == 'manual':
            self.manual_screen = ManualScreen(self.content_frame)
            frame = self.manual_screen.content()
            if frame is not None:
                frame.pack(fill=tk.BOTH, expand=True)
                self.set_active_button(self.manual_button)
            else:
                print('Error: Manual screen content is None')

        elif screen_name == 'about':
            self.about_screen = AboutScreen(self.content_frame)
            frame = self.about_screen.content()
            if frame is not None:
                frame.pack(fill=tk.BOTH, expand=True)
                self.set_active_button(self.about_button)
            else:
                print('Error: About screen content is None')

if __name__ == '__main__':
    home = HomeScreen()
    home.mainloop()
