from rsa import RSAKeyManager 
from aes import AES

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes



class hybrid:

    def __init__(self, rsa_key_manager):
        self.rsa_key_manager = rsa_key_manager

    def encrpt(self, plaintext):
    
      aes = AES()

      ciphertext, tag = aes.AES_encryption(plaintext)

      encrypted_key = self.rsa_key_manager.public_key.encrypt(
          aes.key,
          padding.OAEP(
              mgf=padding.MGF1(algorithm=hashes.SHA256()),
              algorithm=hashes.SHA256(),
              label=None
          )
      )

      return encrypted_key, ciphertext, aes.nonce, tag 

    def decrypt(self, encrypted_key, ciphertext, nonce, tag):

        aes_key = self.rsa_key_manager.private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
     )

        aes = AES(aes_key)

        plaintext = aes.AES_dectryption(ciphertext, nonce, tag)

        return plaintext



        
    











