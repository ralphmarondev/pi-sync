from pyfingerprint.pyfingerprint import PyFingerprint

try:
    f = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)

    if f.verifyPassword():
        print('Sensor initialized successfully.')
    else:
        print('Password error.')

except Exception as e:
    print(f"Initialization failed: {e}")
