from RPLCD.i2c import CharLCD
import time

# Set your LCD address (commonly 0x27 or 0x3f)
lcd = CharLCD('PCF8574', 0x27)

lcd.write_string("Hello from Pi 5!")
time.sleep(3)
lcd.clear()
lcd.write_string("I2C LCD Working!")
