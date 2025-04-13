import customtkinter as ctk

from dashboard import DashboardFrame
from room import RoomFrame
from tenants import TenantsFrame


class NavigationFrame(ctk.CTkFrame):
    def __init__(self, master, main_content):
        super().__init__(master, width=200)
        self.grid_propagate(False)
        self.main_content = main_content  # reference to the main content frame

        # theme remove this later
        ctk.set_appearance_mode('light')
        # ctk.set_default_color_theme('purple_theme.json')
        ctk.set_default_color_theme('green')

        self.dashboard_button = ctk.CTkButton(self, text='D A S H B O A R D', width=180, height=50,
                                              command=self.show_dashboard)
        self.dashboard_button.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')

        self.room_button = ctk.CTkButton(self, text='R O O M', width=180, height=50, command=self.show_room)
        self.room_button.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='w')

        self.tenant_button = ctk.CTkButton(self, text='T E N A N T', width=180, height=50, command=self.show_tenant)
        self.tenant_button.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')

    def show_dashboard(self):
        self.main_content.show_frame(DashboardFrame)

    def show_room(self):
        self.main_content.show_frame(RoomFrame)

    def show_tenant(self):
        self.main_content.show_frame(TenantsFrame)


class MainContentFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frames = {}  # store different frames
        self.current_frame = None

    def show_frame(self, frame_class):
        # replaces the current frame with the requested frame
        if self.current_frame:
            self.current_frame.grid_forget()  # hide current frame

        # Always recreate RoomFrame to refresh its data
        if frame_class in (RoomFrame, TenantsFrame):
            self.frames[frame_class] = frame_class(self)  # recreate to refresh data everytime
        elif frame_class not in self.frames:
            self.frames[frame_class] = frame_class(self)  # create if not exists

        self.current_frame = self.frames[frame_class]
        self.current_frame.grid(row=0, column=0, sticky='nsew')


class HomeScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Home')
        self.geometry('700x480')
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_content_frame = MainContentFrame(self)
        self.main_content_frame.grid(row=0, column=1, padx=(0, 10), pady=10, sticky='nsew')

        self.navigation_frame = NavigationFrame(self, self.main_content_frame)
        self.navigation_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 10),
            sticky='nsw'
        )

        # show dashboard by default
        self.main_content_frame.show_frame(RoomFrame)


if __name__ == '__main__':
    app = HomeScreen()
    app.mainloop()
