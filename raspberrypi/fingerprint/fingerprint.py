from pyfingerprint.pyfingerprint import PyFingerprint
import time

try:
    # Initialize sensor (adjust port if needed)
    f = PyFingerprint('/dev/serial0', 57600, 0xFFFFFFFF, 0x00000000)

    if not f.verifyPassword():
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('Failed to initialize the fingerprint sensor.')
    print('Exception message:', str(e))
    exit(1)

print('Fingerprint sensor initialized.')
print('Currently stored templates:', f.getTemplateCount())
print('Sensor capacity:', f.getStorageCapacity())

try:
    print('\nWaiting for finger...')

    # Wait for finger to be read
    while not f.readImage():
        pass

    # Convert image to characteristics and store in charbuffer 1
    f.convertImage(0x01)

    result = f.searchTemplate()
    positionNumber = result[0]

    if positionNumber >= 0:
        print('Fingerprint already exists at position #', positionNumber)
        exit(0)

    print('Remove finger...')
    time.sleep(2)

    print('Place same finger again...')
    while not f.readImage():
        pass

    # Convert again and store in charbuffer 2
    f.convertImage(0x02)

    # Compare the two
    if f.compareCharacteristics() == 0:
        raise Exception('Fingers do not match.')

    # Create template
    f.createTemplate()

    # Store the template
    positionNumber = f.storeTemplate()
    print('Fingerprint enrolled successfully!')
    print('New template stored at position #', positionNumber)

except Exception as e:
    print('Operation failed.')
    print('Exception message:', str(e))
    exit(1)
