import machine as mn
import utime as ut

ldr = mn.ADC(27)
motor = mn.Pin(15, mn.Pin.OUT)

def get_light(value):
    return 3.3 - (3.3 * float(value) / 65535)

while True:
    ldr_value = ldr.read_u16()

    light = get_light(ldr_value)

    if light < 2:
        motor.high()
    else:
        motor.low()
    
    print("Light:", light)
    ut.sleep(1)