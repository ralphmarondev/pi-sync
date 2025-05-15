import os

TOP_FILE = "upper.txt"
BOTTOM_FILE = "bottom.txt"

# Write text to the top LCD
def write_top(text):
    with open(TOP_FILE, 'w') as file:
        file.write(text[:16])  # Ensure only 16 characters are written

# Write text to the bottom LCD
def write_bottom(text):
    with open(BOTTOM_FILE, 'w') as file:
        file.write(text[:16])  # Ensure only 16 characters are written

# Read text from the top LCD file
def read_top():
    if os.path.exists(TOP_FILE):
        with open(TOP_FILE, 'r') as file:
            return file.read().strip()
    return "Hello"

# Read text from the bottom LCD file
def read_bottom():
    if os.path.exists(BOTTOM_FILE):
        with open(BOTTOM_FILE, 'r') as file:
            return file.read().strip()
    return "World"
