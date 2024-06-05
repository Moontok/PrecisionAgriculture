import machine as mn
import utime as ut


red = mn.Pin(10, mn.Pin.OUT)
yellow = mn.Pin(11, mn.Pin.OUT)
green = mn.Pin(12, mn.Pin.OUT)

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