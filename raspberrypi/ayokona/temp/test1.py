import tkinter as tk
from tkinter import messagebox
import requests
from pyfingerprint.pyfingerprint import PyFingerprint

# Function to initialize the fingerprint sensor and scan the fingerprint
def scan_fingerprint():
    try:
        # Initialize the fingerprint sensor
        f = PyFingerprint('/dev/ttyUSB0', 57600)  # Change to the correct device for your system
        
        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is incorrect!')

        # Wait until a finger is placed on the sensor
        messagebox.showinfo("Fingerprint", "Place your finger on the sensor...")
        
        # Wait for the fingerprint to be read
        while ( f.readImage() == False ):
            pass
        
        # Convert image to template
        f.convertImage(0x01)
        
        # Get the template as a base64 string
        fingerprint_template = f.downloadTemplate(0x01)
        
        # Successfully read fingerprint
        messagebox.showinfo("Fingerprint", "Fingerprint read successfully!")
        
        # Store the template for saving later
        global current_fingerprint
        current_fingerprint = fingerprint_template
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
    
    if current_fingerprint is None:
        messagebox.showerror("Error", "No fingerprint scanned!")
        return

    # Prepare data to send to the API
    data = {
        'name': name,
        'template': current_fingerprint
    }

    # Send data to the API (adjust URL to your API endpoint)
    api_url = "http://localhost:8000/api/fingerprint/enroll/"
    
    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 201:
            messagebox.showinfo("Success", "Fingerprint saved successfully!")
        else:
            messagebox.showerror("Error", f"Error saving fingerprint: {response.json().get('detail')}")
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

# Variable to store the fingerprint template
current_fingerprint = None

# Start the Tkinter main loop
root.mainloop()
