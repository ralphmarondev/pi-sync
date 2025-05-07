from RPLCD.i2c import CharLCD
import time

# Change address below if yours is different (e.g. 0x3F)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A00', auto_linebreaks=True,
              backlight_enabled=True)

try:
    lcd.clear()
    lcd.write_string("Hello, world!")
    lcd.crlf()
    lcd.write_string("Raspberry Pi 5")
    time.sleep(10)

finally:
    lcd.clear()
    lcd.backlight_enabled = False
