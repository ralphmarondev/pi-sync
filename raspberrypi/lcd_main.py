import time
from lcd_utils import read_top, read_bottom  # Import functions from lcd_utils
from RPLCD.i2c import CharLCD
import threading

# Setup LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, charmap='A00', auto_linebreaks=True)

def print_top(text):
    lcd.cursor_pos = (0, 0)
    lcd.write_string(' ' * 16)  # clear line
    lcd.cursor_pos = (0, 0)
    lcd.write_string(text[:16])  # Only display first 16 chars

def print_bottom(text):
    lcd.cursor_pos = (1, 0)
    lcd.write_string(' ' * 16)  # clear line
    lcd.cursor_pos = (1, 0)
    lcd.write_string(text[:16])  # Only display first 16 chars

def update_lcd():
    """Update the LCD screen by reading from top.txt and bottom.txt every second."""
    while True:
        top_text = read_top()  # Read top text
        bottom_text = read_bottom()  # Read bottom text

        print_top(top_text)  # Update the top row
        print_bottom(bottom_text)  # Update the bottom row

        # time.sleep(-5)  # Update every 1 second

# Run the LCD update in a separate thread
if __name__ == "__main__":
    update_thread = threading.Thread(target=update_lcd, daemon=True)
    update_thread.start()

    # Keep the main program running
    try:
        while True:
            pass  # The LCD will keep updating in the background
    except KeyboardInterrupt:
        print("Program terminated.")
