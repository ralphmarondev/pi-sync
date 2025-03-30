import threading
from tkinter import messagebox

import customtkinter as ctk
import requests

from constants import *


# TODO:
#   - implement search
class TenantsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Search Field and New Room Button
        search_frame = ctk.CTkFrame(self)
        search_frame.pack(padx=20, pady=10, fill="x")

        search_frame.grid_columnconfigure(0, weight=1)  # Make column 0 (search entry) expandable
        search_frame.grid_columnconfigure(1, weight=0)  # Make column 1 (new room button) fixed width

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search Tenants...", width=200)
        self.search_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.new_room_button = ctk.CTkButton(search_frame, text="New Tenant", width=120, height=30,
                                             command=self.open_new_tenant_dialog)
        self.new_room_button.grid(row=0, column=1, padx=10, pady=5, sticky='e')

        # Table Frame (Soft Background)
        self.table_frame = ctk.CTkFrame(self, fg_color="#f4f4f4", corner_radius=10)  # Light gray background
        self.table_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Table Headers (Rounded Border Look)
        self.headers = ["Name", "Phone", "Room"]
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
        url = f'{BASE_URL}users/'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                print(data)

                if 'users' in data and isinstance(data['users'], list):
                    self.data = [
                        [
                            user['first_name'] + ' ' + user['last_name'],
                            user['email'] if user['email'] else 'No email',  # fall back if not provided
                            user['registered_doors'],
                            user['id']
                        ]
                        for user in data['users']
                    ]
                    print(self.data)
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
            room_id = entry[3]  # store but not displaying

            for col, value in enumerate(entry[:3]):
                cell = ctk.CTkFrame(self.table_frame, fg_color=bg_color, corner_radius=10)  # Rounded cell
                cell.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
                cell.bind("<Button-1>", lambda event, name=room_name: self.open_tenant_dialog(name))  # Bind click event

                label = ctk.CTkLabel(cell, text=value, font=("Arial", 14), text_color="black")
                label.pack(padx=10, pady=5, fill="both", expand=True)  # Fill entire cell
                label.bind("<Button-1>",
                           lambda event, room_id=room_id: self.open_tenant_dialog(room_id))  # Also bind to label

    def open_tenant_dialog(self, room_id):
        # Fetch the room details based on the id
        room_details = self.fetch_tenant_details(room_id)

        """ Opens a dialog showing the clicked room's name with state, is active status in a combobox, and action buttons """
        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Room Details - {room_details.get('name', room_id)}")

        dialog.transient(self)
        dialog.grab_set()

        # Center the dialog
        self.center_dialog(dialog, width=450, height=250)

        if not room_details or 'name' not in room_details:
            messagebox.showerror('Error', 'Room details are missing the name.')
            return

        # Main Frame for Form (Right side)
        form_frame = ctk.CTkFrame(dialog)
        form_frame.pack(side="right", padx=(0, 10), pady=10, fill="both", expand=True)

        # Label and Entry for the Room Name
        name_label = ctk.CTkLabel(form_frame, text="Room Name", font=("Arial", 14))
        name_label.grid(row=0, column=0, sticky="w", padx=10, pady=(2, 0))

        room_name_var = ctk.StringVar(value=room_details['name'])
        room_name_entry = ctk.CTkEntry(form_frame, textvariable=room_name_var, font=("Arial", 14), width=240)
        room_name_entry.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="ew")

        # Label and Combobox for the State (Open or Closed)
        state_label = ctk.CTkLabel(form_frame, text="State", font=("Arial", 14))
        state_label.grid(row=2, column=0, sticky="w", padx=10, pady=(2, 0))

        state_var = ctk.StringVar(value='Open' if room_details.get('is_open', False) else 'Closed')
        state_combobox = ctk.CTkComboBox(form_frame, values=["Open", "Closed"], variable=state_var, font=("Arial", 14),
                                         width=180)
        state_combobox.grid(row=3, column=0, padx=10, pady=(0, 5), sticky="ew")

        # Label and Combobox for Is Active (Active or Inactive)
        active_label = ctk.CTkLabel(form_frame, text="Is Active", font=("Arial", 14))
        active_label.grid(row=4, column=0, sticky="w", padx=10, pady=(2, 0))

        active_var = ctk.StringVar(value='Active' if room_details.get('is_active', False) else 'Inactive')
        active_combobox = ctk.CTkComboBox(form_frame, values=["Active", "Inactive"], variable=active_var,
                                          font=("Arial", 14), width=180)
        active_combobox.grid(row=5, column=0, padx=10, pady=(0, 5), sticky="ew")

        # Frame for buttons (aligned vertically on the left side, like a nav bar)
        button_frame = ctk.CTkFrame(dialog)
        button_frame.pack(side="left", padx=(10, 10), pady=10, fill="y")

        # Close Button (with color and increased height)
        close_button = ctk.CTkButton(button_frame, text="Close", command=dialog.destroy, fg_color="gray",
                                     hover_color="darkgray", font=("Arial", 14), height=40)
        close_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        # Update Button (with color and increased height)
        update_button = ctk.CTkButton(button_frame, text="Update",
                                      command=lambda: self.update_tenant(room_id, room_name_var.get(), state_var.get(),
                                                                         active_var.get(), dialog), fg_color="green",
                                      hover_color="darkgreen", font=("Arial", 14), height=40)
        update_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Delete Button (with color and increased height)
        delete_button = ctk.CTkButton(button_frame, text="Delete", command=lambda: self.delete_tenant(room_id, dialog),
                                      fg_color="red", hover_color="darkred", font=("Arial", 14), height=40)
        delete_button.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")

    def update_tenant(self, room_id, new_name, new_state, new_status, dialog):
        """ Handle updating the room's name, state, and active status """
        url = f'{BASE_URL}door/update/{room_id}/'  # Assuming this is the endpoint for updating room details
        data = {
            "name": new_name,
            "is_open": new_state == 'Open',
            "is_active": new_status == 'Active'
        }

        try:
            response = requests.put(url, json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Room details updated successfully.")
                dialog.destroy()
                self.fetch_data_from_api()
            else:
                messagebox.showerror("Error", f"Failed to update room: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Network Error", f"Request failed: {e}")

    def delete_tenant(self, room_id, dialog):
        """ Handle deleting the room """
        url = f'{BASE_URL}door/delete/{room_id}/'  # Assuming this is the endpoint for deleting a room
        data = {
            "is_deleted": True
        }

        try:
            response = requests.put(url, json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Room deleted successfully.")
                dialog.destroy()
                self.fetch_data_from_api()
            else:
                messagebox.showerror("Error", f"Failed to delete room: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Network Error", f"Request failed: {e}")

    def fetch_tenant_details(self, room_id):
        """ Fetch details for the specific room using its ID """
        url = f'{BASE_URL}door/{room_id}/'  # Assuming this is the endpoint to fetch details by ID
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()  # Return room details as a dictionary
            else:
                messagebox.showerror('Error', f"Failed to fetch room details: {response.status_code}")
                return {}
        except requests.exceptions.RequestException as e:
            messagebox.showerror('Network Error', f'Request failed: {e}')
            return {}

    def open_new_tenant_dialog(self):
        """Opens a dialog to create a new room."""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Tenant")

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
                                      command=lambda: self.submit_new_tenant(dialog, room_name_entry))
        submit_button.grid(row=0, column=0, padx=10)

        cancel_button = ctk.CTkButton(button_frame, text="Cancel", width=120, height=30, command=dialog.destroy)
        cancel_button.grid(row=0, column=1, padx=10)

    def submit_new_tenant(self, dialog, room_name_entry):
        room_name = room_name_entry.get()
        print(f"Tenant Name: {room_name}")

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
