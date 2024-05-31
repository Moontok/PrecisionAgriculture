from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

def write():
    information = "Bubba"
    id, text = reader.write(information)
    print(f"ID: {id}\n{text}")

write()