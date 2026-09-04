from cryptography.hazmat.primitives import serialization, hashes
#serialization: converts key objetcs from/to bytes, for saving/loading the PEM files
#hashes needed by the OAEP for padding

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
#AES for encrypting the main message

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# for password based key derivation
import os
#os.urandom() for generating secure random keys



class AES:
    def __init__(self, key=None):
        self.key = key or os.urandom(32)
        self.nonce = None

    def AES_encryption(self, plaintext):
        self.nonce = os.urandom(12)
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(self.nonce))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return ciphertext, encryptor.tag

    def AES_dectryption(self, ciphertext, nonce, tag):
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(nonce, tag))
        decryptor = cipher.encryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()
    