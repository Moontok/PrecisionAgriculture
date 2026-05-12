from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522(0, 18, 19, 16, 17, 9)

def write():
    information = "Bubba"
    id, text = reader.write(information)
    print(f"ID: {id}\n{text}")

write()