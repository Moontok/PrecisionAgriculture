from mfrc522 import SimpleMFRC522
import utime as ut


def read():
    print("Reading...Please place the card...")
    id, text = reader.read()
    return id, text

reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

while True:
    info = read()
    print(info)
    ut.sleep(.5)