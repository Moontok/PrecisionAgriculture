import machine as mn
import utime as ut

motor1 = mn.Pin(14, mn.Pin.OUT)
motor2 = mn.Pin(15, mn.Pin.OUT)

def clockwise():
    motor1.high()
    motor2.low()

def stop():
    motor1.low()
    motor2.low()


clockwise()
ut.sleep(2)
stop()