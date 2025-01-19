import tkinter as tk
from tkinter import ttk
import requests

BACKGROUND = '#333333'
FOREGROUND = '#FFFFFF'
FONT_DEFAULT = ('monospace', 16)


class TestCrud(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Test CRUD')
        self.geometry('500x300')
        self.configure(bg=BACKGROUND)

        self.insert_data()

        self.table = ttk.Treeview(self, columns=('name', 'action'), show='headings')
        self.table.heading('name', text='Name')
        self.table.heading('action', text='Action')

        self.table.pack(pady=10)

        self.get_data()

    def insert_data(self):
        frame = tk.Frame(
            master=self,
            bg=BACKGROUND
        )

        label = tk.Label(
            master=frame,
            text='Insert Data',
            bg=BACKGROUND,
            fg=FOREGROUND,
            font=FONT_DEFAULT
        )

        name_entry = tk.Entry(
            master=frame,
            font=FONT_DEFAULT
        )

        insert_button = tk.Button(
            master=frame,
            text='Insert',
            bg='#FF3399',
            font=FONT_DEFAULT,
            command=lambda: self.__insert(name_entry)
        )

        label.grid(row=0, column=0, pady=5)
        name_entry.grid(row=1, column=0, pady=5)
        insert_button.grid(row=2, column=0, pady=5)

        frame.pack(pady=5)

    def __insert(self, name_entry: tk.Entry):
        name = name_entry.get().strip()
        print(f'Name: {name}')

        # Send data to Django
        url = "http://127.0.0.1:8000/test/person/"
        data = {"name": name}
        response = requests.post(url, json=data)

        if response.status_code == 201:
            name_entry.delete(0, tk.END)  # Clear entry field
            print("Data inserted successfully")
            self.get_data()  # Refresh the table
        else:
            print(f"Error inserting data: {response.status_code}")

    def delete_item(self, item_id):
        # Send a DELETE request to Django
        url = f"http://127.0.0.1:8000/test/person/{item_id}/"
        response = requests.delete(url)

        if response.status_code == 204:
            self.table.delete(item_id)  # Remove the item from the table
            print("Item deleted successfully")
        else:
            print(f"Error deleting item: {response.status_code}")

    def get_data(self):
        url = "http://127.0.0.1:8000/test/person/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.table.delete(*self.table.get_children())  # Clear existing data
            for item in data:
                self.table.insert('', 'end', values=(item['name'], item['id']))
                self.__create_delete_button(item)
        else:
            print(f'Error fetching data: {response.status_code}')

    def __create_delete_button(self, item):
        delete_button = tk.Button(self.table, text="Delete", command=lambda item_id=item['id']: self.delete_item(item_id))
        self.table.insert("", "end", values=(item['name'], delete_button))
        delete_button.pack(side="left")


if __name__ == '__main__':
    app = TestCrud()
    app.mainloop()