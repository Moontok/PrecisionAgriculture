import machine as m
import utime as ut

from mfrc522 import SimpleMFRC522
from lcd1602 import LCD


search_id = "270BD233"


rLED = m.Pin(16, m.Pin.OUT)
gLED = m.Pin(17, m.Pin.OUT)
reader = SimpleMFRC522(0, 2, 4, 3, 5, 0)
lcd = LCD()

while True:
    rLED.value(0)
    gLED.value(0)
    lcd.message("Scan Animal Tag")
    tag_id, tag_name = reader.read()
    message = ""

    if tag_id == search_id:
        message = "Match: " + str(tag_name)
        gLED.value(1)
    else:
        message = "No Match: " + str(tag_name)
        rLED.value(1)
    lcd.clear()
    lcd.message(message)
    ut.sleep(3)
    lcd.clear()