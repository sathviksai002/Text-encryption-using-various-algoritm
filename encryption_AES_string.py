from Crypto.Cipher import AES

def pad(entry):
    padded=entry+(16-len(entry)%16)*'['
    return padded
print("1. Encrypt text\n2. Decrypt Text\n3. Exit")
k=""
l=""
cip=""
while True:
    t = int(input("Enter Your Option: "))
    if t==1:
        plain_text=input("Enter text to be encrypted: ")
        plain_text=pad(plain_text)
        plain_text=plain_text.encode('UTF-8')
        print("encoded text with padding done till 16 bits: ",plain_text)
        key=input("Enter key to encrypt the text: ")
        k=key
        key=pad(key)
        key=key.encode('UTF-8')
        l=key
        cipher=AES.new(key,AES.MODE_ECB)
        ciphertext=cipher.encrypt(plain_text)
        print("encrypted cipher form: ",ciphertext)
        cip=ciphertext
        print("**********************Encryption Done************************")
    elif t==2:
        key1=input("Enter key for decryption: ")
        if key1==k:
            cipher2=AES.new(l,AES.MODE_ECB)
            data=cipher.decrypt(cip)
            data=data.decode('UTF-8')
            unpad=data.find('[')
            data=data[:unpad]
            print("Decrypted Data: ",data)
            print("**********************Decryption Done************************")
        else:
            print("Alert!! Wrong Password, Try Again !!!!")
    else:
        print("**********************THANK YOU************************")
        exit(0)