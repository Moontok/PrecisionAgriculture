import machine as mn
import utime as ut


red = mn.Pin(13, mn.Pin.OUT)
yellow = mn.Pin(14, mn.Pin.OUT)
green = mn.Pin(15, mn.Pin.OUT)

while True:
    red.high()
    ut.sleep(1)
    red.low()
    yellow.high()
    ut.sleep(1)
    yellow.low()
    green.high()
    ut.sleep(1)
    green.low()