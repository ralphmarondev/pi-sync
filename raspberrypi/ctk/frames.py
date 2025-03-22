import customtkinter as ctk

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=200) # set width to 200
        self.grid_propagate(False) # prevents shirking to fit contents

        self.checkbox1 = ctk.CTkCheckBox(self, text='checkbox 1')
        self.checkbox1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')

        self.checkbox2 = ctk.CTkCheckBox(self, text='checkbox 2')
        self.checkbox2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='w')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Frames')
        self.geometry('400x180')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10,10),
            sticky='nsw'
        )

if __name__ == '__main__':
    app = App()
    app.mainloop()
