#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
from pyfingerprint.pyfingerprint import PyFingerprint
from RPLCD.i2c import CharLCD

# Setup LCD (adjust address if needed, common ones are 0x27 or 0x3F)
lcd = CharLCD('PCF8574', 0x27)

def lcd_message(line1, line2=''):
    lcd.clear()
    lcd.write_string(line1)
    if line2:
        lcd.crlf()
        lcd.write_string(line2)

try:
    f = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)

    if not f.verifyPassword():
        raise ValueError('Fingerprint sensor password is wrong!')

except Exception as e:
    lcd_message('Sensor Error!', str(e))
    print('Fingerprint sensor could not be initialized!')
    print('Exception message:', str(e))
    sys.exit(1)

lcd_message('Sensor Ready!', 'Templates: {}/{}'.format(
    f.getTemplateCount(), f.getStorageCapacity()))
time.sleep(2)

try:
    lcd_message('Waiting for', 'finger...')
    print('Waiting for finger...')

    while not f.readImage():
        pass

    f.convertImage(0x01)

    result = f.searchTemplate()
    positionNumber = result[0]

    if positionNumber >= 0:
        lcd_message('Already Enrolled', 'Pos #{}'.format(positionNumber))
        print('Template already exists at position #' + str(positionNumber))
        sys.exit(0)

    lcd_message('Remove finger')
    time.sleep(2)

    lcd_message('Place same', 'finger again...')
    print('Waiting for same finger again...')

    while not f.readImage():
        pass

    f.convertImage(0x02)

    if f.compareCharacteristics() == 0:
        raise Exception('Fingers do not match')

    f.createTemplate()

    positionNumber = f.storeTemplate()
    lcd_message('Enroll Success!', 'Pos #{}'.format(positionNumber))
    print('Finger enrolled successfully!')
    print('New template position #' + str(positionNumber))

except Exception as e:
    lcd_message('Enroll Failed!', str(e)[:16])  # Shorten error to fit LCD
    print('Operation failed!')
    print('Exception message:', str(e))
    sys.exit(1)
