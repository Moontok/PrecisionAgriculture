from mfrc522 import SimpleMFRC522
import utime as ut


def read():
    print("Reading...Please place the card...")
    id, text = reader.read()
    return id, text

reader = SimpleMFRC522(0, 18, 16, 19, 17, 9)

while True:
    info = read()
    print(info)
    ut.sleep(.5)