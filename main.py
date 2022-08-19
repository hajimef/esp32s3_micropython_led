from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(48, Pin.OUT)
np = NeoPixel(pin, 1)
while True:
    np[0] = (255, 0, 0)
    np.write()
    time.sleep(1)
    np[0] = (0, 255, 0)
    np.write()
    time.sleep(1)
    np[0] = (0, 0, 255)
    np.write()
    time.sleep(1)
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(1)
