import tkinter as tk
from tkinter import messagebox
import requests
from pyfingerprint.pyfingerprint import PyFingerprint

# Variable to store the template position number
current_fingerprint_position = None

# Function to initialize the fingerprint sensor and scan the fingerprint
def scan_fingerprint():
    global current_fingerprint_position

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
            current_fingerprint_position = positionNumber
            return False

        # Store template at first available position
        positionNumber = f.storeTemplate()
        current_fingerprint_position = positionNumber

        messagebox.showinfo("Fingerprint", f"Fingerprint stored at position {positionNumber}")
        return True

    except Exception as e:
        messagebox.showerror("Error", f"Error while scanning: {str(e)}")
        return False

# Function to save fingerprint data to the API
def save_fingerprint():
    name = name_entry.get()

    if not name:
        messagebox.showerror("Error", "Name cannot be empty!")
        return

    if current_fingerprint_position is None:
        messagebox.showerror("Error", "No fingerprint scanned!")
        return

    # Prepare data to send to the API
    data = {
        'name': name,
        'position': current_fingerprint_position
    }

    api_url = "http://192.168.1.98:8000/api/fingerprint/enroll/"

    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 201:
            messagebox.showinfo("Success", "Fingerprint saved successfully!")
        else:
            messagebox.showerror("Error", f"Error saving fingerprint: {response.json().get('detail', 'Unknown error')}")
    except Exception as e:
        messagebox.showerror("Error", f"Error connecting to API: {str(e)}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Fingerprint Registration")

# Create the name label and entry field
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the scan fingerprint button
scan_button = tk.Button(root, text="Scan Fingerprint", command=scan_fingerprint)
scan_button.grid(row=1, column=0, columnspan=2, pady=10)

# Create the save button
save_button = tk.Button(root, text="Save", command=save_fingerprint)
save_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
root.mainloop()
