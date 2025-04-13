from functools import partial

import customtkinter as ctk


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.frame_width = 150
        self.frame_padding = 20

        # Title
        self.title = ctk.CTkLabel(self, text="Dashboard", font=("Arial", 20, "bold"))
        self.title.grid(row=0, column=0, sticky="w", padx=20, pady=(10, 0))

        # Grid container
        self.grid_container = ctk.CTkFrame(self)
        self.grid_container.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Sample data
        self.door_data = self.get_door_data()

        # Track current column count
        self.current_columns = None

        # Initial draw
        self.after(100, self.check_and_draw_grid)

        # Redraw on resize
        self.bind("<Configure>", self.on_resize)

    def get_door_data(self):
        return [
            {"id": 1, "name": "A14", "is_active": True, "is_open": False, "tenant_count": 1},
            {"id": 2, "name": "A16", "is_active": False, "is_open": False, "tenant_count": 0},
            {"id": 3, "name": "B14", "is_active": True, "is_open": True, "tenant_count": 2},
            {"id": 4, "name": "B16", "is_active": True, "is_open": False, "tenant_count": 3},
            {"id": 5, "name": "C14", "is_active": True, "is_open": False, "tenant_count": 1},
            {"id": 6, "name": "C16", "is_active": False, "is_open": False, "tenant_count": 0},
            {"id": 7, "name": "D14", "is_active": True, "is_open": True, "tenant_count": 2},
            {"id": 8, "name": "D16", "is_active": True, "is_open": False, "tenant_count": 3},
        ]

    def check_and_draw_grid(self):
        container_width = self.grid_container.winfo_width()
        if container_width <= 1:
            self.after(100, self.check_and_draw_grid)  # Wait until layout stabilizes
        else:
            self.create_door_grid(force=True)

    def create_door_grid(self, force=False):
        for widget in self.grid_container.winfo_children():
            widget.destroy()

        container_width = self.grid_container.winfo_width()
        if container_width <= 1:
            container_width = self.winfo_width()

        total_space = self.frame_width + self.frame_padding
        columns = max(1, container_width // total_space)

        if columns == self.current_columns and not force:
            return

        self.current_columns = columns

        for index, door in enumerate(self.door_data):
            row = index // columns
            col = index % columns

            door_frame = ctk.CTkFrame(self.grid_container, width=self.frame_width, height=self.frame_width)
            door_frame.grid(row=row, column=col, padx=10, pady=10)
            door_frame.grid_propagate(False)

            door_name = door["name"]
            door_status = "Open" if door["is_open"] else "Closed"
            label = ctk.CTkLabel(door_frame, text=f"{door_name}\n{door_status}", font=("Arial", 14))
            label.pack(expand=True)

            # Make whole frame clickable
            door_frame.bind("<Button-1>", partial(self.on_door_click, door["id"]))
            label.bind("<Button-1>", partial(self.on_door_click, door["id"]))

    def on_resize(self, event):
        self.create_door_grid()

    def on_door_click(self, door_id, event=None):
        print(f"Door {door_id} clicked.")
