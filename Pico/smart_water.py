import machine as mn
import utime as ut

motor = mn.Pin(14, mn.Pin.OUT)

sensor = mn.ADC(28)

def start():
    motor.high()

def stop():
    motor.low()

while True:
    value = sensor.read_u16()
    if value < 5000:
        start()
        ut.sleep(1)
    else:
        stop()