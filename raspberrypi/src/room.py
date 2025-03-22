import customtkinter as ctk

class RoomFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Search Field and New Room Button
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(padx=20, pady=10, fill="x")

        # Configure search frame grid to make button align to the right
        search_frame.grid_columnconfigure(0, weight=1)  # Make column 0 (search entry) expandable
        search_frame.grid_columnconfigure(1, weight=0)  # Make column 1 (new room button) fixed width

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search Room...", width=200)
        self.search_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.new_room_button = ctk.CTkButton(search_frame, text="New Room", width=120, height=30,
                                             command=self.open_new_room_dialog)
        self.new_room_button.grid(row=0, column=1, padx=10, pady=5, sticky='e')

        # Table Frame (Soft Background)
        table_frame = ctk.CTkFrame(self, fg_color="#f4f4f4", corner_radius=10)  # Light gray background
        table_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Table Headers (Rounded Border Look)
        headers = ["Name", "Tenants", "Active", "State"]
        header_color = "#d1e7dd"  # Soft pastel green
        for col, header in enumerate(headers):
            cell = ctk.CTkFrame(table_frame, fg_color=header_color, corner_radius=10)  # Rounded header
            cell.grid(row=0, column=col, padx=3, pady=3, sticky="nsew")
            label = ctk.CTkLabel(cell, text=header, font=("Arial", 16, "bold"), text_color="black")
            label.pack(padx=10, pady=5)

        # Sample Data (With a Cute Soft Style)
        data = [
            ["Room 101", "4", "Yes", "Open"],
            ["Room 102", "3", "No", "Close"],
            ["Room 103", "1", "Yes", "Close"],
        ]

        row_colors = ["#ffffff", "#f8f9fa"]  # Alternating soft white and light gray
        for row, entry in enumerate(data, start=1):
            bg_color = row_colors[row % 2]  # Alternate row colors
            for col, value in enumerate(entry):
                cell = ctk.CTkFrame(table_frame, fg_color=bg_color, corner_radius=10)  # Rounded cell
                cell.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
                label = ctk.CTkLabel(cell, text=value, font=("Arial", 14), text_color="black")
                label.pack(padx=10, pady=5)

        # Adjust column weights so they stretch nicely
        for col in range(len(headers)):
            table_frame.columnconfigure(col, weight=1)

    def open_new_room_dialog(self):
        # Create a new Toplevel window (Dialog)
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Room")

        # Set the dialog to stay on top of the main window
        dialog.transient(self)  # Makes the dialog window stay on top of the main window
        dialog.grab_set()  # Ensures no interaction with the main window until the dialog is closed

        # Room Name entry with label on top
        room_name_label = ctk.CTkLabel(dialog, text="Room Name:")
        room_name_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        room_name_entry = ctk.CTkEntry(dialog, width=250)
        room_name_entry.grid(row=1, column=0, padx=10, pady=(0, 10))
        room_name_entry.insert(0, "")  # Default value

        # Buttons below (Submit and Cancel)
        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")  # Frame for buttons
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        submit_button = ctk.CTkButton(button_frame, text="Submit", width=120, height=30,
                                      command=lambda: self.submit_new_room(dialog, room_name_entry))
        submit_button.grid(row=0, column=0, padx=10)

        cancel_button = ctk.CTkButton(button_frame, text="Cancel", width=120, height=30, command=dialog.destroy)
        cancel_button.grid(row=0, column=1, padx=10)

    def submit_new_room(self, dialog, room_name_entry):
        # Collect data from the room name entry
        room_name = room_name_entry.get()

        # Print the collected data (for now)
        print(f"Room Name: {room_name}")

        # Close the dialog
        dialog.destroy()
