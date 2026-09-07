from algorithm.rsa import RSAKeyManager 
from algorithm.aes import AES

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes



class hybrid:

    def __init__(self, rsa_key_manager):
        self.rsa_key_manager = rsa_key_manager

    def encrpt(self, plaintext):

      aes = AES()

      signature = self.rsa_key_manager.private_key.sign(
       plaintext.encode(),
       padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
        hashes.SHA256()
)
      
    

      ciphertext, tag = aes.AES_encryption(plaintext)

      encrypted_key = self.rsa_key_manager.public_key.encrypt(
          aes.key,
          padding.OAEP(
              mgf=padding.MGF1(algorithm=hashes.SHA256()),
              algorithm=hashes.SHA256(),
              label=None
          )
      )

      return encrypted_key, ciphertext, aes.nonce, tag, signature

    def decrypt(self, encrypted_key, ciphertext, nonce, tag, signature, p_key):

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

       
        p_key.verify(
            signature,
            plaintext,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
)

        return plaintext.decode()



        
    











