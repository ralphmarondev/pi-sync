import threading
from tkinter import messagebox

import customtkinter as ctk
import requests

from constants import *

class RoomFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Search Field and New Room Button
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(padx=20, pady=10, fill="x")

        search_frame.grid_columnconfigure(0, weight=1)  # Make column 0 (search entry) expandable
        search_frame.grid_columnconfigure(1, weight=0)  # Make column 1 (new room button) fixed width

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search Room...", width=200)
        self.search_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.new_room_button = ctk.CTkButton(search_frame, text="New Room", width=120, height=30,
                                             command=self.open_new_room_dialog)
        self.new_room_button.grid(row=0, column=1, padx=10, pady=5, sticky='e')

        # Table Frame (Soft Background)
        self.table_frame = ctk.CTkFrame(self, fg_color="#f4f4f4", corner_radius=10)  # Light gray background
        self.table_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Table Headers (Rounded Border Look)
        self.headers = ["Name", "Tenants", "Active", "State"]
        header_color = "#d1e7dd"  # Soft pastel green
        self.column_sorting = [None] * len(self.headers)  # Track sorting order for each column

        for col, header in enumerate(self.headers):
            cell = ctk.CTkFrame(self.table_frame, fg_color=header_color, corner_radius=10)  # Rounded header
            cell.grid(row=0, column=col, padx=3, pady=3, sticky="nsew")

            # Bind the entire header frame to be clickable
            cell.bind("<Button-1>", lambda event, col=col: self.sort_table(col))

            label = ctk.CTkLabel(cell, text=header, font=("Arial", 16, "bold"), text_color="black")
            label.pack(padx=10, pady=5, fill="both", expand=True)  # Center the text and make it fill the cell

            # Also bind the label in case user clicks directly on text
            label.bind("<Button-1>", lambda event, col=col: self.sort_table(col))

        # Threading to fetch data from API
        self.data = []
        self.fetch_thread = threading.Thread(target=self.fetch_data_from_api)
        self.fetch_thread.daemon = True
        self.fetch_thread.start()

        self.row_colors = ["#ffffff", "#f8f9fa"]  # Alternating soft white and light gray
        self.display_table()

        # Adjust column weights
        for col in range(len(self.headers)):
            self.table_frame.columnconfigure(col, weight=1)

    def fetch_data_from_api(self):
        url = f'{BASE_URL}doors/'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # format according to table columns
                self.data = [
                    [
                        door['name'],
                        door['id'],
                        'Yes' if door['is_active'] else 'No',
                        'Open' if door['is_open'] else 'Closed',
                    ]
                    for door in data
                ]
                # once the data is fetched, update the UI
                self.after(0, self.display_table)
            else:
                print(f'Error: {response.status_code}, {response.json()}')
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')

    def sort_table(self, column_index):
        # Toggle sorting order for the clicked column
        if self.column_sorting[column_index] is None:
            self.column_sorting[column_index] = "asc"
        elif self.column_sorting[column_index] == "asc":
            self.column_sorting[column_index] = "desc"
        else:
            self.column_sorting[column_index] = "asc"

        # Sort the data based on the selected column and order
        reverse = True if self.column_sorting[column_index] == "desc" else False
        self.data.sort(key=lambda x: x[column_index], reverse=reverse)

        # Re-display the sorted table
        self.display_table()

    def display_table(self):
        # Clear previous table content (except the header)
        for widget in self.table_frame.winfo_children():
            if widget not in self.table_frame.grid_slaves(row=0):
                widget.grid_forget()

        # Display sorted data
        for row, entry in enumerate(self.data, start=1):
            bg_color = self.row_colors[row % 2]  # Alternate row colors
            room_name = entry[0]  # Room name (first column)

            for col, value in enumerate(entry):
                cell = ctk.CTkFrame(self.table_frame, fg_color=bg_color, corner_radius=10)  # Rounded cell
                cell.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
                cell.bind("<Button-1>", lambda event, name=room_name: self.open_room_dialog(name))  # Bind click event

                label = ctk.CTkLabel(cell, text=value, font=("Arial", 14), text_color="black")
                label.pack(padx=10, pady=5, fill="both", expand=True)  # Fill entire cell
                label.bind("<Button-1>",
                           lambda event, name=room_name: self.open_room_dialog(name))  # Also bind to label

    def open_room_dialog(self, room_name):
        """ Opens a dialog showing the clicked room's name """
        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Room Details - {room_name}")

        dialog.transient(self)
        dialog.grab_set()

        # Center the dialog
        self.center_dialog(dialog, width=300, height=150)

        label = ctk.CTkLabel(dialog, text=f"Room: {room_name}", font=("Arial", 16))
        label.pack(padx=20, pady=20)

        close_button = ctk.CTkButton(dialog, text="Close", command=dialog.destroy)
        close_button.pack(pady=10)

    def open_new_room_dialog(self):
        """Opens a dialog to create a new room."""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Room")

        dialog.transient(self)
        dialog.grab_set()

        # Center the dialog
        self.center_dialog(dialog, width=280, height=200)

        room_name_label = ctk.CTkLabel(dialog, text="Room Name:")
        room_name_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        room_name_entry = ctk.CTkEntry(dialog, width=260)
        room_name_entry.grid(row=1, column=0, padx=10, pady=(0, 10))

        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        submit_button = ctk.CTkButton(button_frame, text="Submit", width=120, height=30,
                                      command=lambda: self.submit_new_room(dialog, room_name_entry))
        submit_button.grid(row=0, column=0, padx=10)

        cancel_button = ctk.CTkButton(button_frame, text="Cancel", width=120, height=30, command=dialog.destroy)
        cancel_button.grid(row=0, column=1, padx=10)

    def submit_new_room(self, dialog, room_name_entry):
        room_name = room_name_entry.get()
        print(f"Room Name: {room_name}")

        def post_room_data():
            try:
                data = {'name': room_name}
                url = f'{BASE_URL}door/new/'
                response = requests.post(url, data=data)

                if response.status_code == 201:  # created
                    print('Room created successfully!')
                    messagebox.showinfo('Success', 'Room created successfully!')
                    self.fetch_data_from_api()
                else:
                    print(f'Error: {response.status_code}, {response.json()}')
                    messagebox.showerror('Error', f'Failed to create room: {response.status_code}')
            except requests.exceptions.RequestException as e:
                print(f'Request failed: {e}')
                messagebox.showerror('Network Error', f'Request failed: {e}')

            except Exception as e:
                print(f'An unexpected error occurred: {e}')
                messagebox.showerror('Error', f'An unexpected error occurred: {e}')
            finally:
                dialog.destroy()

        threading.Thread(target=post_room_data, daemon=True).start()

    def center_dialog(self, dialog, width=300, height=200):
        """Centers the given dialog on the main window."""
        self.update_idletasks()  # Ensure geometry updates before getting values

        main_x = self.winfo_rootx()
        main_y = self.winfo_rooty()
        main_width = self.winfo_width()
        main_height = self.winfo_height()

        x_offset = main_x + (main_width - width) // 2
        y_offset = main_y + (main_height - height) // 2

        dialog.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
