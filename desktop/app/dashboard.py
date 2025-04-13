from functools import partial

import customtkinter as ctk


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Reduced frame width (half of the previous value)
        self.frame_width = 75
        self.frame_padding = 20
        self.default_container_width = (self.frame_width + self.frame_padding) * 2 + 40

        # Grid container with fixed width
        self.grid_container = ctk.CTkFrame(self, width=self.default_container_width)
        self.grid_container.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        self.grid_container.grid_propagate(False)

        # Only 2 doors
        self.door_data = [
            {"id": 1, "name": "A14", "is_active": True, "is_open": False, "tenant_count": 1},
            {"id": 2, "name": "A16", "is_active": False, "is_open": True, "tenant_count": 0},
            {"id": 1, "name": "A14", "is_active": True, "is_open": False, "tenant_count": 1},
            {"id": 2, "name": "A16", "is_active": False, "is_open": True, "tenant_count": 0},
            {"id": 1, "name": "A14", "is_active": True, "is_open": False, "tenant_count": 1},
            {"id": 2, "name": "A16", "is_active": False, "is_open": True, "tenant_count": 0},
        ]

        self.create_door_grid()

    def create_door_grid(self):
        for index, door in enumerate(self.door_data):
            col = index % 2
            row = index // 2

            # Door frame with border and margin
            outer_frame = ctk.CTkFrame(
                self.grid_container,
                corner_radius=10,
                border_width=2,
                border_color="gray",
                fg_color="transparent",  # Light background
                bg_color='transparent'
            )
            outer_frame.grid(row=row, column=col, padx=10, pady=10, sticky="n")
            outer_frame.configure(width=self.frame_width, height=self.frame_width)
            outer_frame.grid_propagate(False)

            # Inner padding using an inner frame
            inner_frame = ctk.CTkFrame(outer_frame, fg_color="transparent")
            inner_frame.pack(expand=True, fill="both", padx=10, pady=10)

            door_name = door["name"]
            door_status = "Open" if door["is_open"] else "Closed"
            label = ctk.CTkLabel(inner_frame, text=f"{door_name}\n{door_status}", font=("Arial", 14),
                                 width=self.frame_width, height=self.frame_width)
            label.pack(expand=True)

            # Make entire area clickable
            outer_frame.bind("<Button-1>", partial(self.on_door_click, door["id"]))
            label.bind("<Button-1>", partial(self.on_door_click, door["id"]))
            inner_frame.bind("<Button-1>", partial(self.on_door_click, door["id"]))

    def on_door_click(self, door_id, event=None):
        print(f"Door {door_id} clicked.")
