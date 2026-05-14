# Reset all the pins on the raspberry pi pico

import machine as mn


PINS_NO_RESET = [23, 24, 25] # These pins are used for the onboard LED and USB communication, so we won't reset them

def reset_pins():
    for i in range(29):
        if i not in PINS_NO_RESET:
            pin = mn.Pin(i, mn.Pin.OUT)
            pin.low()


if __name__ == "__main__":
    reset_pins()