import dht
import machine as mn
import utime

pin = mn.Pin(15, mn.Pin.IN, mn.Pin.PULL_UP)
sensor = dht.DHT11(pin)

while True:
    sensor.measure()
    temp = sensor.temperature()
    f_temp = temp * 9/5 + 32
    hum = sensor.humidity()

    print("Temperature:", f_temp, "F")
    print("Humidity:", hum, "%")
    print()
    utime.sleep(1)