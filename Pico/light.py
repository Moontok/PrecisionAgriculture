import machine as mn
import utime as ut


light = mn.ADC(27)

while True:
    value = light.read_u16()
    value = 3.3 * float(value) / 65535
    print(value)
    ut.sleep(1)
