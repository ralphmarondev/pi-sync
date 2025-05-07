from RPLCD.i2c import CharLCD

# Setup
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, charmap='A00', auto_linebreaks=True)

def print_top(text):
    lcd.cursor_pos = (0, 0)
    lcd.write_string(' ' * 16)  # clear line
    lcd.cursor_pos = (0, 0)
    lcd.write_string(text[:16])

def print_bottom(text):
    lcd.cursor_pos = (1, 0)
    lcd.write_string(' ' * 16)  # clear line
    lcd.cursor_pos = (1, 0)
    lcd.write_string(text[:16])

def clear_lcd():
    lcd.clear()
