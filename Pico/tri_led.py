import machine as mn
import utime as ut


def set_color(leds, r, g, b):
    leds[0].duty_u16(65535 * r)
    leds[1].duty_u16(65535 * g)
    leds[2].duty_u16(65535 * b)

r_led = mn.PWM(mn.Pin(10))
g_led = mn.PWM(mn.Pin(11))
b_led = mn.PWM(mn.Pin(12))

leds = [r_led, g_led, b_led]

for led in leds:
    led.freq(1000)

while True:
    set_color(leds, 1, 0, 0)
    ut.sleep(.5)
    set_color(leds, 0, 1, 0)
    ut.sleep(.5)
    set_color(leds, 0, 0, 1)
    ut.sleep(.5)