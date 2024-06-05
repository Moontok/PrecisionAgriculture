import machine as mn
import utime as ut
import math

therm = mn.ADC(28)
ldr = mn.ADC(27)
motor = mn.Pin(15, mn.Pin.OUT)

def get_temp(value):
    Vr = 3.3 * float(value) / 65535
    Rt = 10000 * Vr / (3.3 - Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    c = temp - 273.15
    f = c * 1.8 + 32
    return f

def get_light(value):
    return 3.3 * float(value) / 65535

while True:
    therm_value = therm.read_u16()
    ldr_value = ldr.read_u16()

    temp = get_temp(therm_value)
    light = get_light(ldr_value)

    if temp > 75 or light < 2:
        motor.high()
    else:
        motor.low()
    
    print("Temperature:", temp, "F")
    print("Light:", light)
    ut.sleep(1)