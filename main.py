def Encrypt(filename,key):
    file= open(filename,"rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open("CC-"+ filename,"wb")
    file.write(data)
    file.close()
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open("CC-" + filename, "wb")
    file.write(data)
    file.close()

choice=""
while choice!="3":
    print("Enter the option")
    print("1. Encrypt the file")
    print("2. Decrypt the file")
    print("3. Quit")
    choice = input()
    if choice=="1" or choice=="2":
        key = int(input("Enter the key\n"))
        filename=input("Enter filename exe:\n")
    if choice =="1":
        Encrypt(filename, key)
    if choice =="2":
        Decrypt(filename,key)