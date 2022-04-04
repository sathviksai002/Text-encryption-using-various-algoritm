import rsa

public_key, private_key = rsa.newkeys(1024)
em=""
print("1. Encrypt text\n2. Decrypt Text\n3. Exit")
while True:
    t=int(input("Enter your option: "))
    if t==1:
        message = input("Enter the message: ")
        res = bytes(message,'utf-8')
        # print(res)
        eme=rsa.encrypt(res,public_key)
        # print(eme)
        em=eme
        print("**********************Encryption Done************************")
    elif t==2:
        dm=rsa.decrypt(em,private_key)
        print(dm.decode())
        print("**********************Decryption Done************************")
    else:
        print("**********************THANK YOU************************")
        exit(1)
        exit(1)
