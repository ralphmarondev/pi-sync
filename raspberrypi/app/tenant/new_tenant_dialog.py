import tkinter as tk

class NewTenantDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New Tenant")
        self.geometry("300x200")

        self.first_name_label = tk.Label(self, text="First Name:")
        self.first_name_label.pack(pady=5)
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.pack(pady=5)

        self.last_name_label = tk.Label(self, text="Last Name:")
        self.last_name_label.pack(pady=5)
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.pack(pady=5)

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        self.submit_button = tk.Button(self, text="Add Tenant", command=self.add_tenant)
        self.submit_button.pack(pady=20)

    def add_tenant(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        print(f"Adding new tenant: {first_name} {last_name} - {email}")
        # Here you would add the new tenant to your data model or database.
        self.destroy()  # Close the dialog
