import machine as mn
import utime as ut

motor1 = mn.Pin(14, mn.Pin.OUT)
motor2 = mn.Pin(15, mn.Pin.OUT)

sensor = mn.ADC(28)

def clockwise():
    motor1.high()
    motor2.low()

def stop():
    motor1.low()
    motor2.low()


while True:
    value = sensor.read_u16()
    if value < 5000:
        clockwise()
        ut.sleep(1)
    else:
        stop()