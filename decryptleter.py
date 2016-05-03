from simplecrypt import encrypt, decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

f = open('passwords.txt', 'r')

for line in f:
    try:
        print(line)
        plaintext = decrypt(line.strip(), encrypted)
        print(plaintext)
    except:
        print("Not he")

    #print(plaintext)