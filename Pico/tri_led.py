import machine as mn
import utime as ut


def set_color(leds, r, g, b):
    red = int(65535 * r)
    green = int(65535 * g)
    blue = int(65535 * b)
    
    leds[0].duty_u16(red)
    leds[1].duty_u16(green)
    leds[2].duty_u16(blue)

r_led = mn.PWM(mn.Pin(13))
g_led = mn.PWM(mn.Pin(14))
b_led = mn.PWM(mn.Pin(15))

leds = [r_led, g_led, b_led]

for led in leds:
    led.freq(1000)

while True:
    set_color(leds, .5, .5, 0)
    ut.sleep(.5)
    set_color(leds, 0, .5, .5)
    ut.sleep(.5)
    set_color(leds, .5, 0, .5)
    ut.sleep(.5)