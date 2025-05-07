from RPLCD.i2c import CharLCD
import time

# LCD setup (adjust address if needed)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, charmap='A00', auto_linebreaks=True)

try:
    while True:
        lcd.clear()
        lcd.write_string('SMART DOOR')
        lcd.cursor_pos = (1, 0)  # second line
        lcd.write_string(time.strftime('%H:%M:%S'))  # current time
        time.sleep(1)  # refresh every second

except KeyboardInterrupt:
    print("\n🛑 Stopped by user.")
    lcd.clear()
