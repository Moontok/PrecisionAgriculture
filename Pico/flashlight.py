import machine as mn


def set_color(leds, r, g, b):
    leds[0].duty_u16(65535 * r)
    leds[1].duty_u16(65535 * g)
    leds[2].duty_u16(65535 * b)

r_led = mn.PWM(mn.Pin(10))
g_led = mn.PWM(mn.Pin(11))
b_led = mn.PWM(mn.Pin(12))

button = mn.Pin(16, mn.Pin.IN, mn.Pin.PULL_DOWN)

leds = [r_led, g_led, b_led]

for led in leds:
    led.freq(1000)

while True:
    if button.value() == 1:
        set_color(leds, 1, 1, 1)
    else:
        set_color(leds, 0, 0, 0)