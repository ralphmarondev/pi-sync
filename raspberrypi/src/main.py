import customtkinter as ctk


class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('PiSync')
        self.geometry('400x300')

        hello = ctk.CTkLabel(self, text='Hello there!')
        hello.grid(row=0, column=0, pady=10, padx=10)


app = MyApp()
app.mainloop()
