from pyfingerprint.pyfingerprint import PyFingerprint

try:
    f = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)

    if f.verifyPassword() == False:
        raise ValueError('The given fingerprint sensor password is wrong!')

    print('Sensor initialized, waiting for finger...')

    # Wait for finger to be placed
    while f.readImage() == False:
        print('No finger detected...')
    
    print('Finger detected!')

except Exception as e:
    print('Error: ' + str(e))
