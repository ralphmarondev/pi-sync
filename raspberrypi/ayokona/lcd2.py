from RPLCD.i2c import CharLCD
import time

# LCD setup (usually address 0x27 or 0x3f, bus 1)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, charmap='A00', auto_linebreaks=True)

# Clear and display message
lcd.clear()
lcd.write_string('Hello World!')

time.sleep(5)
lcd.clear()


lcd.write_string('Ralph is cute :)')
time.sleep(5)
lcd.clear()
lcd.write('Hehehhee')
time.sleep(50)