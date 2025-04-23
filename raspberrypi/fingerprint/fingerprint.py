from pyfingerprint.pyfingerprint import PyFingerprint
import time

try:
    f = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)

    if f.verifyPassword() is False:
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('Failed to initialize the sensor!')
    print('Exception message: ' + str(e))
    exit()

print('Currently used templates: ' + str(f.getTemplateCount()) + '/' + str(f.getStorageCapacity()))

try:
    print('Waiting for finger...')

    # Wait for finger to be read
    while f.readImage() == False:
        pass

    # Converts read image to characteristics and stores in charbuffer 1
    f.convertImage(0x01)

    # Check for existing fingerprint
    result = f.searchTemplate()
    positionNumber = result[0]

    if positionNumber >= 0:
        print('Fingerprint already exists at position #' + str(positionNumber))
        exit()

    print('Remove finger...')
    time.sleep(2)

    print('Place the same finger again...')
    while f.readImage() == False:
        pass

    # Converts read image to characteristics and stores in charbuffer 2
    f.convertImage(0x02)

    # Compare the two fingerprints
    if f.compareCharacteristics() == 0:
        raise Exception('Fingers do not match!')

    # Create a template
    f.createTemplate()

    # Store template at the next available position
    positionNumber = f.storeTemplate()
    print('Fingerprint enrolled successfully!')
    print('New fingerprint stored at position #' + str(positionNumber))

except Exception as e:
    print('Enrollment failed!')
    print('Exception message: ' + str(e))
    exit()
