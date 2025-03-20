import tkinter as tk

class UpdateRoomDialog:
    def __init__(self, parent, room_name, tenant_count, is_active, update_callback):
        self.parent = parent
        self.room_name = room_name
        self.tenant_count = tenant_count
        self.is_active = is_active
        self.update_callback = update_callback

        self.dialog = tk.Toplevel(parent)
        self.dialog.title(f'Update {self.room_name}')

        # Room name (readonly)
        tk.Label(self.dialog, text='Room Name').grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.dialog, text=self.room_name, font=('Arial', 10, 'italic')).grid(row=0, column=1, padx=10, pady=5)

        # Tenant Count
        tk.Label(self.dialog, text='Tenant Count').grid(row=1, column=0, padx=10, pady=5)
        self.tenant_count_entry = tk.Entry(self.dialog)
        self.tenant_count_entry.insert(0, str(self.tenant_count))
        self.tenant_count_entry.grid(row=1, column=1, padx=10, pady=5)

        # isActive
        tk.Label(self.dialog, text='Active (Yes/No)').grid(row=2, column=0, padx=10, pady=5)
        self.is_active_entry = tk.Entry(self.dialog)
        self.is_active_entry.insert(0, self.is_active)
        self.is_active_entry.grid(row=2, column=1, padx=10, pady=5)

        # Save button
        save_button = tk.Button(self.dialog, text='Save', command=self.save_changes)
        save_button.grid(row=3, column=0, columnspan=2, pady=10)

    def save_changes(self):
        """ Save the updated values and close the dialog. """
        new_tenant_count = int(self.tenant_count_entry.get())
        new_is_active = self.is_active_entry.get()
        self.update_callback(self.room_name, new_tenant_count, new_is_active)
        self.dialog.destroy()
