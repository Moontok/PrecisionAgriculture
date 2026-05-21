import machine as mn
import utime as ut

motor = mn.Pin(15, mn.Pin.OUT)

sensor = mn.ADC(28)

while True:
    value = sensor.read_u16()
    if value < 5000:
        motor.high()
        ut.sleep(1)
    else:
        motor.low()