from functools import partial

import customtkinter as ctk


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Configure the grid with no weight for the rows and columns
        self.grid_rowconfigure(0, weight=1)  # Adjust the first row for the title
        self.grid_columnconfigure(0, weight=1)  # Adjust the first column for the title

        # Fetching door data from the API
        self.door_data = self.get_door_data()

        # Create a grid of clickable frames based on the data
        self.create_door_grid()

    def get_door_data(self):
        # Simulating API call for door data (replace with your actual API request)
        response = [
            {"id": 1, "name": "A14", "is_active": True, "is_open": False, "tenant_count": 1},
            {"id": 2, "name": "A16", "is_active": False, "is_open": False, "tenant_count": 0},
            {"id": 3, "name": "B14", "is_active": True, "is_open": True, "tenant_count": 2},
            {"id": 4, "name": "B16", "is_active": True, "is_open": False, "tenant_count": 3},
            # Add more doors here if needed
        ]
        return response

    def create_door_grid(self):
        # Create a frame for each door dynamically
        for i, door in enumerate(self.door_data):
            door_frame = ctk.CTkFrame(self, width=150, height=150)  # Set fixed size for each door frame
            door_frame.grid(row=(i // 4), column=i % 4, padx=10, pady=10, sticky="nsew")  # Adjust grid size

            door_name = door["name"]
            door_status = "Open" if door["is_open"] else "Closed"
            door_label = ctk.CTkLabel(door_frame, text=f"{door_name}\n{door_status}", font=("Arial", 14))
            door_label.pack(pady=10)

            # Use functools.partial to bind the correct door_id
            door_frame.bind("<Button-1>", partial(self.on_door_click, door["id"]))

    def on_door_click(self, door_id, event=None):
        print(f"Door {door_id} clicked.")
        # You can add functionality to handle click events, such as opening or closing the door
        # or displaying more information.


# Example usage in your app (HomeScreen)
if __name__ == "__main__":
    app = ctk.CTk()  # Main application window
    home_screen = HomeScreen(app)
    home_screen.pack(fill="both", expand=True)  # Fill the window with the HomeScreen
    app.mainloop()
