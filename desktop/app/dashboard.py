from functools import partial

import customtkinter as ctk


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.frame_width = 75
        self.frame_padding = 20
        self.default_container_width = (self.frame_width + self.frame_padding) * 2 + 40

        self.grid_container = ctk.CTkFrame(self, width=self.default_container_width)
        self.grid_container.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        self.grid_container.grid_propagate(False)

        self.door_data = [
            {"id": 1, "name": "A14", "is_active": True, "is_open": False, "tenant_count": 1},
            {"id": 2, "name": "A16", "is_active": False, "is_open": True, "tenant_count": 0}
        ]

        # Store widgets for dynamic updates
        self.door_widgets = {}

        self.create_door_grid()

    def create_door_grid(self):
        for index, door in enumerate(self.door_data):
            col = index % 2
            row = index // 2

            outer_frame = ctk.CTkFrame(
                self.grid_container,
                corner_radius=10,
                border_width=2,
                border_color="green" if door["is_open"] else "red",
                fg_color="transparent",
                bg_color='transparent'
            )
            outer_frame.grid(row=row, column=col, padx=10, pady=10, sticky="n")
            outer_frame.configure(width=self.frame_width, height=self.frame_width)
            outer_frame.grid_propagate(False)

            inner_frame = ctk.CTkFrame(outer_frame, fg_color="transparent")
            inner_frame.pack(expand=True, fill="both", padx=10, pady=10)

            label = ctk.CTkLabel(
                inner_frame,
                text=f"{door['name']}\n{'Open' if door['is_open'] else 'Closed'}",
                font=("Arial", 14),
                width=self.frame_width,
                height=self.frame_width
            )
            label.pack(expand=True)

            # Bind all clickable areas
            for widget in (outer_frame, inner_frame, label):
                widget.bind("<Button-1>", partial(self.on_door_click, door["id"]))

            # Store for future updates
            self.door_widgets[door["id"]] = {
                "frame": outer_frame,
                "label": label,
                "data": door
            }

    def on_door_click(self, door_id, event=None):
        print(f"Door {door_id} clicked.")

        door_widget = self.door_widgets[door_id]
        door_data = door_widget["data"]
        door_data["is_open"] = not door_data["is_open"]  # Toggle state

        # Update label and border color
        new_status = "Open" if door_data["is_open"] else "Closed"
        door_widget["label"].configure(text=f"{door_data['name']}\n{new_status}")
        new_border_color = "green" if door_data["is_open"] else "red"
        door_widget["frame"].configure(border_color=new_border_color)
