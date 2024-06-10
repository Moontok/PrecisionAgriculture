import machine as mn
import utime as ut


red = mn.Pin(16, mn.Pin.OUT)

while True:
    red.high()
    ut.sleep(1)
    red.low()
    ut.sleep(1)
