import customtkinter as ctk
import requests
import threading
from tkinter import messagebox

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

        self.new_tenant_button = ctk.CTkButton(search_frame, text="New Tenant", width=120, height=30,
                                               command=self.open_new_tenant_dialog)
        self.new_tenant_button.grid(row=0, column=1, padx=10, pady=5, sticky='e')

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
                            f"{user['first_name']} {user['last_name']}",
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
            tenant_name = entry[0]
            tenant_id = entry[3]

            for col, value in enumerate(entry[:3]):
                cell = ctk.CTkFrame(self.table_frame, fg_color=bg_color, corner_radius=10)  # Rounded cell
                cell.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
                cell.bind("<Button-1>",
                          lambda event, name=tenant_name: self.open_tenant_dialog(name))  # Bind click event

                label = ctk.CTkLabel(cell, text=value, font=("Arial", 14), text_color="black")
                label.pack(padx=10, pady=5, fill="both", expand=True)  # Fill entire cell
                label.bind("<Button-1>",
                           lambda event, tenant_id=tenant_id: self.open_tenant_dialog(tenant_id))  # Also bind to label

    def open_tenant_dialog(self, tenant_id):
        print(f'Opening tenant dialog with id: {tenant_id}')
        tenant_details = self.fetch_tenant_details(tenant_id)
        print(tenant_details)

        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Tenant Details - {tenant_details.get('first_name', tenant_id)}")

        dialog.transient(self)
        dialog.grab_set()

        # Center the dialog
        self.center_dialog(dialog, width=450, height=250)

        if not tenant_details or 'username' not in tenant_details:
            messagebox.showerror('Error', 'Tenant details are missing the name.')
            return

        # Main Frame for Form (Right side)
        form_frame = ctk.CTkFrame(dialog)
        form_frame.pack(side="right", padx=(0, 10), pady=10, fill="both", expand=True)

        # Label and Entry for the Tenant Name
        name_label = ctk.CTkLabel(form_frame, text="Tenant Name", font=("Arial", 14))
        name_label.grid(row=0, column=0, sticky="w", padx=10, pady=(2, 0))

        tenant_name_var = ctk.StringVar(value=tenant_details['first_name'])
        tenant_name_entry = ctk.CTkEntry(form_frame, textvariable=tenant_name_var, font=("Arial", 14), width=240)
        tenant_name_entry.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="ew")

        username_label = ctk.CTkLabel(form_frame, text="Tenant Username", font=("Arial", 14))
        username_label.grid(row=0, column=0, sticky="w", padx=10, pady=(2, 0))

        tenant_username_var = ctk.StringVar(value=tenant_details['username'])
        tenant_username_entry = ctk.CTkEntry(form_frame, textvariable=tenant_username_var, font=("Arial", 14),
                                             width=240)
        tenant_username_entry.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="ew")

        # Frame for buttons (aligned vertically on the left side, like a nav bar)
        button_frame = ctk.CTkFrame(dialog)
        button_frame.pack(side="left", padx=(10, 10), pady=10, fill="y")

        # Close Button (with color and increased height)
        close_button = ctk.CTkButton(button_frame, text="Close", command=dialog.destroy, fg_color="gray",
                                     hover_color="darkgray", font=("Arial", 14), height=40)
        close_button.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")

        # Update Button (with color and increased height)
        update_button = ctk.CTkButton(button_frame, text="Update",
                                      command=lambda: self.update_tenant(tenant_id, tenant_name_var.get(),
                                                                         state_var.get(),
                                                                         active_var.get(), dialog), fg_color="green",
                                      hover_color="darkgreen", font=("Arial", 14), height=40)
        update_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Delete Button (with color and increased height)
        delete_button = ctk.CTkButton(button_frame, text="Delete",
                                      command=lambda: self.delete_tenant(tenant_id, dialog),
                                      fg_color="red", hover_color="darkred", font=("Arial", 14), height=40)
        delete_button.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")

    def update_tenant(self, tenant_id, first_name, last_name, username, password, dialog):
        """ Handle updating the tenant's name, state, and active status """
        url = f'{BASE_URL}user/update/{tenant_id}/'
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'password': password
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

    def delete_tenant(self, tenant_id, dialog):
        """ Handle deleting the tenant """
        url = f'{BASE_URL}user/delete/{tenant_id}/'
        data = {
            "is_deleted": True
        }

        try:
            response = requests.put(url, json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Tenant deleted successfully.")
                dialog.destroy()
                self.fetch_data_from_api()
            else:
                messagebox.showerror("Error", f"Failed to delete tenant from database: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Network Error", f"Request failed: {e}")

    def fetch_tenant_details(self, tenant_id):
        """ Fetch details for the specific tenant using its ID """
        url = f'{BASE_URL}user/{tenant_id}/'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()  # Return tenant details as a dictionary
            else:
                messagebox.showerror('Error', f"Failed to fetch tenant details: {response.status_code}")
                return {}
        except requests.exceptions.RequestException as e:
            messagebox.showerror('Network Error', f'Request failed: {e}')
            return {}

    def open_new_tenant_dialog(self):
        PADY_LABEL = (5, 0)
        PADY_ENTRY = (0, 5)
        """Opens a dialog to create a new tenant."""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Tenant")

        dialog.transient(self)
        dialog.grab_set()

        # Center the dialog
        self.center_dialog(dialog, width=560, height=400)

        # first row
        first_name_label = ctk.CTkLabel(dialog, text="First Name:")
        first_name_label.grid(row=0, column=0, padx=10, pady=PADY_LABEL, sticky="w")
        first_name_entry = ctk.CTkEntry(dialog, width=260)
        first_name_entry.grid(row=1, column=0, padx=10, pady=PADY_ENTRY)

        last_name_label = ctk.CTkLabel(dialog, text="Last Name:")
        last_name_label.grid(row=0, column=1, padx=10, pady=PADY_LABEL, sticky="w")
        last_name_entry = ctk.CTkEntry(dialog, width=260)
        last_name_entry.grid(row=1, column=1, padx=10, pady=PADY_ENTRY)

        # second row
        username_label = ctk.CTkLabel(dialog, text="Username:")
        username_label.grid(row=2, column=0, padx=10, pady=PADY_LABEL, sticky="w")
        username_entry = ctk.CTkEntry(dialog, width=260)
        username_entry.grid(row=3, column=0, padx=10, pady=PADY_ENTRY)

        password_label = ctk.CTkLabel(dialog, text="Password:")
        password_label.grid(row=2, column=1, padx=10, pady=PADY_LABEL, sticky="w")
        password_entry = ctk.CTkEntry(dialog, width=260)
        password_entry.grid(row=3, column=1, padx=10, pady=PADY_ENTRY)

        # Third row
        hint_password_label = ctk.CTkLabel(dialog, text="Password hint:")
        hint_password_label.grid(row=4, column=0, padx=10, pady=PADY_LABEL, sticky="w")
        hint_password_entry = ctk.CTkEntry(dialog, width=260)
        hint_password_entry.grid(row=5, column=0, padx=10, pady=PADY_ENTRY)

        options = ["Male", "Female"]

        # Create combo box
        gender_label = ctk.CTkLabel(dialog, text="Gender:")
        gender_label.grid(row=4, column=1, padx=10, pady=PADY_LABEL, sticky="w")
        gender_combobox = ctk.CTkComboBox(dialog, values=options, width=260)
        gender_combobox.grid(row=5, column=1, pady=PADY_ENTRY)
        # gender_combobox.set(options[0])  # default value 'Male'
        gender_combobox.set("Select Gender")  # Optional placeholder

        # Fourth row [buttons]
        button_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        button_frame.grid(row=8, column=0, columnspan=2, pady=10)

        submit_button = ctk.CTkButton(
            button_frame,
            text="Register",
            width=260,
            height=35,
            command=lambda: self.submit_new_tenant(
                dialog,
                first_name_entry,
                last_name_entry,
                username_entry,
                password_entry,
                hint_password_entry,
                gender_combobox
            )
        )
        submit_button.grid(row=0, column=0, padx=10, pady=10)

        cancel_button = ctk.CTkButton(button_frame, text="Cancel", width=260, height=35, command=dialog.destroy)
        cancel_button.grid(row=0, column=1, padx=10, pady=10)

    def submit_new_tenant(
            self,
            dialog,
            first_name_entry,
            last_name_entry,
            username_entry,
            password_entry,
            hint_password_entry,
            gender_combobox
    ):
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        password_hint = hint_password_entry.get()
        gender = gender_combobox.get()

        print(f"Adding new tenants...")
        print(f'First name: {first_name}')
        print(f'Last name: {last_name}')
        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Password hint: {password_hint}')
        print(f'Gender: {gender}')

        def post_room_data():
            try:
                data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'username': username,
                    'password': password,
                    'hint_password': password_hint,
                    'gender': gender,
                    'is_superuser': False
                }
                url = f'{BASE_URL}register/'
                response = requests.post(url, data=data)

                if response.status_code == 201:  # created
                    print('Tenant created successfully!')
                    messagebox.showinfo('Success', 'Tenant created successfully!')
                    self.fetch_data_from_api()
                else:
                    print(f'Error: {response.status_code}, {response.json()}')
                    messagebox.showerror('Error', f'Failed to register tenant: {response.status_code}')
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
