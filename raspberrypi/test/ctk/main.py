import customtkinter as ctk

# window properties
root = ctk.CTk()
root.geometry('800x500')
root.title('Toggle Side Menu')

# functions
def on_hover(e):
    home_button.configure(fg_color='#FF7575', bg_color='#FF7575', text_color='black')

def on_leave(e):
    home_button.configure(fg_color='gray17', bg_color='gray17', text_color='#FF7575')

def on_hover2(e):
    settings_button.configure(fg_color='#FF7575', bg_color='#FF7575', text_color='black')

def on_leave2(e):
    settings_button.configure(fg_color='gray17', bg_color='gray17', text_color='#FF7575')

# content
def remove():
    main_frame = ctk.CTkFrame(root, width=800, height=550, fg_color='transparent')
    main_frame.place(x=0, y=0)

    open_button = ctk.CTkButton(root, text='O P E N', width=100, height=50, fg_color='transparent',
                                 bg_color='transparent', hover_color='red')
    open_button.place(x=0, rely=0.005)

def toggle():
    global home_button, settings_button
    side_menu = ctk.CTkFrame(root, width=200, height=800)
    side_menu.place(x=0, y=0.5)

    close_button = ctk.CTkButton(root, text='C L O S E', width=100, height=50, fg_color='transparent',
                                 bg_color='transparent', hover_color='red')
    close_button.place(x=0, rely=0.005)

    home_button = ctk.CTkButton(root, text='H O M E', width=200, height=50, fg_color='transparent', bg_color='transparent',
                                text_color='#FF7575')
    home_button.place(x=0, rely=0.1)

    settings_button = ctk.CTkButton(root, text='S E T T I N G S', width=200, height=50, fg_color='transparent',
                                    bg_color='transparent', text_color='#FF7575')
    settings_button.place(x=0, rely=0.2)

# customization
home_button.bind('<Enter>', on_hover)
home_button.bind('<Leave>', on_leave)

settings_button.bind('<Enter>', on_hover2)
settings_button.bind('<Leave>', on_leave2)

if __name__ == '__main__':
    root.mainloop()
