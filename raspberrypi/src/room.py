import customtkinter as ctk

class RoomFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Title Label
        title_label = ctk.CTkLabel(self, text="Room", font=("Arial", 24, "bold"))
        title_label.pack(pady=10)

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

