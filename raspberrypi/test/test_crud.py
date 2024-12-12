import tkinter as tk

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

        # send data to django
        url = "http://127.0.0.1:8000/test/person/"
        data = {"name": name}
        response = requests.post(url, json=data)

        if response.status_code == 201:
            name_entry.delete(0, tk.END)  # clear entry field
            print('Data inserted successfully')
        else:
            print(f'Error: {response.status_code}')


if __name__ == '__main__':
    app = TestCrud()
    app.mainloop()
