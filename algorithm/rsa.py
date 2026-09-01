#importing all the libraries from the cryptography module

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
# RSA key generatiion + OAEP padding for the encryption of EAS key

from cryptography.hazmat.primitives import serialization, hashes
#serializaation for converting from to binary data and to save/load the PEM files
#hashes needed by the OAEP for padding

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
#AES for encrypting the main message

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from cryptography.hazmat.primitives import keywrap
# needed in encrypting symmetric key into Asymmetric key

import os
#to import built_in OS module



class RSAKeyManager:

    def __init__(self, key_size=1028):
        self.key_size = 1028
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size = self.key_size)
        self.public_key = self.private_key.public_key()

    def serialize_private_key(self, password = none):
        encryption = serialization.BestAvailableEncryption(password) if password else serialization.NoEncryption
        return self.private_key.private_bytes(
            encoding= serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm = encryption 
        )

    def serialize_public_key(self):
         return self.public_key.public_bytes(
                    encoding= serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )

    def load_private_key(self, pem_data, password = none):
        self.private_key = serialization.load_pem_private_key(pem_data, password)
        self.public_key = self.private_key.public_key()

    def load_public_key(self, pem_data):
        self.public_key = serialization.load_pem_public_key(pem_data)

