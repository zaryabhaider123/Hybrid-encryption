#importing all the libraries from the cryptography module

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
# RSA key generation + OAEP padding for the encryption of AES key

from cryptography.hazmat.primitives import serialization, hashes
#serialization: converts key objetcs from/to bytes, for saving/loading the PEM files
#hashes needed by the OAEP for padding


import os
#os.urandom() for generating secure random keys



class RSAKeyManager:

    # Constructor for RSAKeyManager
    #key_size = size of the key in bits (Recommended by NIST : 2048)
    #public key and private key start as none until generate_key is called
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.public_key = None
        self.private_key = None

    #Method for generating key pairs,
    #the function "generate_private_key" is Crytography library fuction
    #Public exponent = 65537 as default and recommended
    def generate_keys(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size = self.key_size)
        self.public_key = self.private_key.public_key()

    # serialize the private key to PEM bytes, optionally password encrypted
    def serialize_private_key(self, password = None):
        encryption = serialization.BestAvailableEncryption(password) if password else serialization.NoEncryption()
        return self.private_key.private_bytes(
            encoding= serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm = encryption 
        )

     # Method to  convert public key into bytes 
    def serialize_public_key(self):
         return self.public_key.public_bytes(
                    encoding= serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )

    #This method loads the previously saved private key from PEM bytes
    def load_private_key(self, pem_data, password = None):
        self.private_key = serialization.load_pem_private_key(pem_data, password)
        self.public_key = self.private_key.public_key()

    #This method loads the previously saved public key from PEM bytes
    def load_public_key(self, pem_data):
        self.public_key = serialization.load_pem_public_key(pem_data)

