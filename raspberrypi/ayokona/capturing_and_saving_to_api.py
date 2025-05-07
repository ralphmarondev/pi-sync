import tkinter as tk
from tkinter import messagebox
import requests
import base64
from pyfingerprint.pyfingerprint import PyFingerprint

# Variable to store the fingerprint template (Base64-encoded string)
current_fingerprint_template = None
user_name = None  # Variable to store the user's name

# Function to initialize the fingerprint sensor and clear its memory
def clear_fingerprint_memory():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600)

        if not f.verifyPassword():
            raise ValueError('Incorrect fingerprint sensor password!')

        # Clear the sensor memory
        f.clearDatabase()
        messagebox.showinfo("Fingerprint", "Fingerprint memory cleared successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"Error clearing fingerprint memory: {str(e)}")

# Function to initialize the fingerprint sensor and scan the fingerprint
def scan_fingerprint():
    global current_fingerprint_template, user_name

    if user_name is None:
        messagebox.showerror("Error", "Please register a user first!")
        return

    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600)

        if not f.verifyPassword():
            raise ValueError('Incorrect fingerprint sensor password!')

        messagebox.showinfo("Fingerprint", "Place your finger on the sensor...")

        while not f.readImage():
            pass

        f.convertImage(0x01)

        # Check if this fingerprint already exists
        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber >= 0:
            messagebox.showinfo("Fingerprint", f"Fingerprint already exists at position {positionNumber}")
            return False

        # Store template at first available position
        positionNumber = f.storeTemplate()

        # Download and encode characteristics
        characteristics = f.downloadCharacteristics(0x01)
        characteristics_bytes = bytearray(characteristics)
        template_b64 = base64.b64encode(characteristics_bytes).decode('utf-8')

        current_fingerprint_template = template_b64

        messagebox.showinfo("Fingerprint", f"Fingerprint stored at position {positionNumber}.\n\nTemplate (Base64):\n{template_b64}")
        return True

    except Exception as e:
        messagebox.showerror("Error", f"Error while scanning: {str(e)}")
        return False

# Function to save fingerprint data to the API
def save_fingerprint():
    global user_name

    if user_name is None:
        messagebox.showerror("Error", "Please register a user first!")
        return

    if current_fingerprint_template is None:
        messagebox.showerror("Error", "No fingerprint scanned!")
        return

    data = {
        'name': user_name,
        'template': current_fingerprint_template
    }

    api_url = "http://192.168.1.98:8000/api/fingerprint/enroll/"

    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 201:
            messagebox.showinfo("Success", f"Fingerprint saved successfully!\n\nTemplate:\n{current_fingerprint_template}")
        else:
            messagebox.showerror("Error", f"Error saving fingerprint: {response.json().get('detail', 'Unknown error')}")
    except Exception as e:
        messagebox.showerror("Error", f"Error connecting to API: {str(e)}")

# Function to register user
def register_user():
    global user_name
    user_name = name_entry.get()

    if not user_name:
        messagebox.showerror("Error", "Name cannot be empty!")
        return

    # Clear fingerprint memory before starting the registration process
    clear_fingerprint_memory()

    messagebox.showinfo("Registration", f"User {user_name} registered. Please scan fingerprint now.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Fingerprint Registration")

# Create the name label and entry field
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the register button
register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=1, column=0, columnspan=2, pady=10)

# Create the scan fingerprint button
scan_button = tk.Button(root, text="Scan Fingerprint", command=scan_fingerprint)
scan_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create the save button
save_button = tk.Button(root, text="Save", command=save_fingerprint)
save_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
root.mainloop()
