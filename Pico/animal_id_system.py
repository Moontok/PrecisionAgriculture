import machine as m
import utime as ut

from mfrc522 import SimpleMFRC522
from lcd1602 import LCD


search_id = "270BD233" # Tag ID to search for

reader = SimpleMFRC522(0, 18, 19, 16, 17, 9)
lcd = LCD()

while True:
    lcd.message("Scan Animal Tag")
    tag_id, tag_name = reader.read()
    message = ""

    lcd.clear()
    if tag_id == search_id:
        message = "Match: " + str(tag_name)
    else:
        message = "No Match: " + str(tag_name)

    lcd.message(message)
    ut.sleep(3)
    lcd.clear()