import machine as mn
import utime as ut


led = mn.Pin(10, mn.Pin.OUT)

led.high()
ut.sleep(2)
led.low()