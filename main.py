from algorithm.rsa import RSAKeyManager 
from algorithm.aes import AES
from algorithm.hybrid import hybrid
import base64
from cryptography.hazmat.primitives import serialization

rsa_manager = RSAKeyManager()
rsa_manager.generate_keys()


h = hybrid(rsa_manager)

print("-----The Encryptor-----")


while True:
    print('''Select the mode:
1 - Encrypt
2 - Decrypt
3 - Show public key
4 - Exit''')
    mode = int(input("Enter the mode number : "))
    if mode == 1:

        print("You choose enctrytion")
        print("Plain text :")
        text = input()
        encrypted_key, ciphertext, nonce, tag, sign = h.encrpt(text)

        print("Output")
        print("Ciphertext : " , base64.b64encode(ciphertext).decode())
        print("AES encrypted key : ",  base64.b64encode(encrypted_key).decode())
        print("Nonce : ", base64.b64encode(nonce).decode())
        print("Tag : ", base64.b64encode(tag).decode())
        print("Signature : " , base64.b64encode(sign).decode())

    elif mode == 2:

        print("You choose dectrytion")

        print("Enter the ciphertext :")
        cipher = base64.b64decode(input())
        print("Enter the AES encrypted key :")
        encrypted_key = base64.b64decode(input())
        print("Enter the sender's public key :")
        p_key = base64.b64decode(input())
        public_key = serialization.load_pem_public_key(p_key)
        print("Enter the tag :")
        tag = base64.b64decode(input())
        print("Enter the nonce :")
        nonce = base64.b64decode(input())
        print("Enter the signature :")
        sign = base64.b64decode(input())
        

        h.decrypt(encrypted_key, cipher, nonce, tag, sign, public_key)

    elif mode == 3:
        key = rsa_manager.public_key
        key = rsa_manager.serialize_public_key()
        key = base64.b64encode(key).decode()

        print("Public Key : ",key )

    elif mode == 4:
        break

    else:
        print("Please select options from menu")


   




