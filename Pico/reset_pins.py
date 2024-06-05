# Reset all the pins on the raspberry pi pico

import machine as mn


def reset_pins():
    for i in range(29):
        pin = mn.Pin(i, mn.Pin.IN)
        pin.low()


if __name__ == "__main__":
    reset_pins()