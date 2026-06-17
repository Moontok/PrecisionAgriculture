import machine as mn
import utime as ut


red = mn.Pin(17, mn.Pin.OUT)
yellow = mn.Pin(19, mn.Pin.OUT)
green = mn.Pin(20, mn.Pin.OUT)

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