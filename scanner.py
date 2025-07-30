import time
from pyfingerprint.pyfingerprint import PyFingerprint
import os

SAVE_PATH = 'saved/your_fingerprint.bmp'

def enroll_and_save():
    try:
        sensor = PyFingerprint('COM4', 57600, 0xFFFFFFFF, 0x00000000)
        if not sensor.verifyPassword():
            raise ValueError("Wrong password!")
    except Exception as e:
        print("Sensor init error:", e)
        return False

    print('Place finger to enroll...')
    while not sensor.readImage():
        pass

    sensor.convertImage(0x01)
    sensor.createTemplate()
    sensor.downloadImage(SAVE_PATH)
    print("Fingerprint saved at", SAVE_PATH)
    return True

def capture_fingerprint():
    try:
        sensor = PyFingerprint('COM3', 57600, 0xFFFFFFFF, 0x00000000)
        if not sensor.verifyPassword():
            raise ValueError('Incorrect sensor password!')
    except Exception as e:
        print('Sensor init failed:', e)
        return "error"

    print('Waiting for finger...')
    for _ in range(100):
        if sensor.readImage():
            break
        time.sleep(0.1)
    else:
        print('No finger detected')
        return "fail"

    sensor.convertImage(0x01)
    if not os.path.exists(SAVE_PATH):
        print("No saved fingerprint. Please enroll first.")
        return "fail"

    sensor.uploadImage(SAVE_PATH)
    result = sensor.searchTemplate()
    position = result[0]

    if position == -1:
        print('No match found!')
        return "fail"
    else:
        print('Match found!')
        return "MATCH_123"
