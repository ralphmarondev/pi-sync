import tkinter as tk
from tkinter import ttk

class RoomScreen:
    def __init__(self, parent_frame):
        self.root = parent_frame
        self.table = None
        self.sorting_order = {}  # Track sorting order for each column

    def content(self):
        dashboard_frame = tk.Frame(self.root)

        # title label, can be a search field later
        title_label = tk.Label(dashboard_frame, text='Rooms', font=('Arial', 14, 'bold'))
        title_label.pack(pady=(10, 5))

        # Define columns
        columns = ('Name', 'Tenant', 'isActive')
        self.table = ttk.Treeview(dashboard_frame, columns=columns, show='headings')

        # Define column headings
        for col in columns:
            self.table.heading(col, text=col, command=lambda c=col: self.sort_column(c))
            self.sorting_order[col] = False  # Default: ascending order

        # Define column widths
        self.table.column('Name', width=150, anchor='center')
        self.table.column('Tenant', width=50, anchor='center')
        self.table.column('isActive', width=80, anchor='center')

        # Style to change the background of the heading
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Arial', 10, 'bold'), background='white', foreground='#4A90E2')

        # Apply custom style to frame to simulate header background color
        header_frame = tk.Frame(dashboard_frame, bg='#4A90E2')  # Header background color
        header_frame.pack(fill='x')

        self.table.pack(fill='both', expand=True, padx=5, pady=5)

        # Insert sample data
        self.data = [
            ('A14', 5, 'Yes'),
            ('A15', 3, 'No'),
            ('A16', 4, 'Yes'),
        ]
        self.populate_table()

        # Bind click event to open menu
        self.table.bind('<ButtonRelease-1>', self.handle_click)

        return dashboard_frame

    def populate_table(self):
        """ Clears and repopulates the table with sorted data. """
        for row in self.table.get_children():
            self.table.delete(row)

        for row in self.data:
            self.table.insert('', 'end', values=row)

    def sort_column(self, column):
        """ Sort table data when clicking a column heading. """
        col_index = {'Name': 0, 'Tenant': 1, 'isActive': 2}[column]
        self.sorting_order[column] = not self.sorting_order[column]  # Toggle sorting order

        self.data.sort(key=lambda x: x[col_index], reverse=self.sorting_order[column])
        self.populate_table()

    def handle_click(self, event):
        """ Show menu when clicking any row. """
        row_id = self.table.identify_row(event.y)

        if row_id:
            values = self.table.item(row_id, 'values')
            if values:
                room_name, tenant_count, is_active = values
                self.show_action_menu(event, room_name)

    def show_action_menu(self, event, room_name):
        """ Display action menu when clicking any row. """
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label='View Details', command=lambda: self.view_details(room_name))
        menu.add_command(label='Update', command=lambda: self.update_room(room_name))
        menu.add_command(label='Delete', command=lambda: self.delete_room(room_name))
        menu.post(event.x_root, event.y_root)

    def view_details(self, room_name):
        print(f'Viewing details for room: {room_name}')

    def update_room(self, room_name):
        print(f'Updating room: {room_name}')

    def delete_room(self, room_name):
        print(f'Deleting room: {room_name}')
        self.data = [row for row in self.data if row[0] != room_name]
        self.populate_table()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x300')

    content_frame = tk.Frame(root)
    room = RoomScreen(content_frame)
    frame = room.content()

    frame.pack(fill=tk.BOTH, expand=True)
    content_frame.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
