from functools import partial

import customtkinter as ctk


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Optional: Add a title
        title = ctk.CTkLabel(self, text="Dashboard", font=("Arial", 20, "bold"))
        title.grid(row=0, column=0, pady=10)

        # Create a container for the door grid
        self.grid_container = ctk.CTkFrame(self)
        self.grid_container.grid(row=1, column=0, padx=20, pady=20)

        # Door data
        self.door_data = self.get_door_data()

        # Create the grid
        self.create_door_grid()

    def get_door_data(self):
        # Simulated API response
        return [
            {"id": 1, "name": "A14", "is_active": True, "is_open": False, "tenant_count": 1},
            {"id": 2, "name": "A16", "is_active": False, "is_open": False, "tenant_count": 0},
            {"id": 3, "name": "B14", "is_active": True, "is_open": True, "tenant_count": 2},
            {"id": 4, "name": "B16", "is_active": True, "is_open": False, "tenant_count": 3},
            # Add more as needed
        ]

    def create_door_grid(self):
        columns = 4  # Customize number of columns per row

        for index, door in enumerate(self.door_data):
            row = index // columns
            col = index % columns

            # Create the door frame with fixed size
            door_frame = ctk.CTkFrame(self.grid_container, width=150, height=150, corner_radius=10)
            door_frame.grid(row=row, column=col, padx=10, pady=10)
            door_frame.grid_propagate(False)  # Prevent content from resizing the frame

            # Label inside door frame
            door_name = door["name"]
            door_status = "Open" if door["is_open"] else "Closed"
            label = ctk.CTkLabel(door_frame, text=f"{door_name}\n{door_status}", font=("Arial", 14))
            label.pack(expand=True)

            # Make it clickable
            door_frame.bind("<Button-1>", partial(self.on_door_click, door["id"]))
            label.bind("<Button-1>", partial(self.on_door_click, door["id"]))  # Ensure label also reacts

    def on_door_click(self, door_id, event=None):
        print(f"Door {door_id} clicked.")
