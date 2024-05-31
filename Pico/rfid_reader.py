from mfrc522 import SimpleMFRC522
import utime as ut

def read():
    print("Reading...Please place the card...")
    id, text = reader.read()
    return id, text

search_id = "270BD233"

reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

searching = True

while searching:
    info = read()
    print(
        f'ID: {info[0]}\n{info[1]}'
    )
    if info[0] == search_id:
        print("Animal found!")
        searching = False
    else:
        print("Animal not found. Please try again.")
    ut.sleep(.5)