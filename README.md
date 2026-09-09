<h1>Hybrid Encryption CLI</h1>
A command line tool for encrypting and decrypting messages using hybrid encryption which includes RSA and AES algorithms, with digital signature for authentication and integration.

<h2>Overview</h2>
This tool lets users encrypt and decrypt the message using the RSA and AES algorithm. This is the same encryption pattern used in TLS, HTTPS and SSH for secure encryption. The program uses AES to encrypt the text and then uses RSA to encrypt the AES key. It was built as hands-on learning to understand how encryption schemes work under the hood instead of relying on a single library call.

<h2>Features:</h2>  

* RSA key pair generation.  
* AES-GCM for encrypting actual message.  
* RSA-OAEP encryption to securely wrap the AES key.  
* RSA-PSS for authentication.   
* Base64 encoded output for copying, pasting and sharing as plain text.  
* Interactive command line menu to encrypt, decrypt and share your public key.  

<h2>Cryptographic decision:</h2>

<h4>Why hybrid instead of pure RSA?</h4>
RSA is well suited for key exchange but it’s not practical for encrypting the entire message directly. Its block size is limited by the key size( around 190 bytes for 2048 bit key) and its underlying modular exponentiation is comparatively more expensive than the symmetric encryption. Hybrid resolves both issues by dividing the work, AES handles the actual message since it's fast and has no meaningful size limit while RSA is used only to encrypt a small, fixed size AES key giving RSA key exchange security without compromising on its performance.
 
 
 <h4>Why AES-256 over AES-128?</h4>
Both AES-256 and AES-128 are exceptionally secure and approved encryption standards but AES-256 uses larger keys and more processing rounds. However, the main reason for choosing AES-256 was to match the strength of RSA as RSA was using a 2048 bit key. So, both sides of hybrid encryption have similar strength in security. The extra computation cost of AES-256 over AES-128 is negligible at the scale of short text messages so added security comes with no real performance cost.


<h4>Why GCM mode?</h4>
The GCM mode combines AES with counter mode for encryption and Galois mode for authentication. They ensure both the confidentiality and integrity of data. It generates a tag that detects any tampering with cipher text. 


<h4>Why a 12 bytes nonce?</h4>
The standard recommended size of nonce for AES-GCM  is 12 bytes (96 bits). It skips the GHASH function and is used directly to construct the initial counter. In the case of other sizes like 8 or 16 bytes , it would require the GHASH function to perform extra hash operations to convert them.


<h4>Why OAEP for encryption and PSS for signing?</h4>
Raw RSA is deterministic. If you encrypt the same message twice with the same public key, you will have identical cipher text. This predictability leaks information and is unsuitable for secure encryption. To fix this OAEP transforms the message before encryption. It adds a random seed, a mask generating function and a hash of an optional label (often left empty). On the other hand,  PSS uses a randomized signature for the same message thus it is probabilistic. In this signing scheme a random salt is added in the signature process.


<h2>Encryption Flow:</h2>
Generate a random AES key  
Encrypt message with AES-256-GCM  
Hash  and sign the plaintext with sender’s private RSA key (PSS)  
Encrypt the AES key with receiver’s RSA public key (OAEP)  
Output : Cipher text, AES encrypted key, nonce, tag, signature  

<h4>Decryption Flow:</h4>

Decrypt the AES key using the RSA private key  
Decrypt the cipher text using recovered AES key  
Verify the signature against the decrypted plain text using sender’s public key  
Output: original plaintext (only if signature verification succeeds )  

<h2>Usage:</h2>
Upon running the program, a menu appears with 4 options

1. Encrypt
2. Decrypt
3. Show public key
4. Exit  


If the user chooses to encrypt, type the message to encrypt and copy the five values (cipher text, AES encrypted key, nonce, tag, signature). 
If you select decrypt, enter the cipher text, AES encrypted key, nonce, tag, sender’s RSA public key and signature. If the signature succeeds, the original plaintext is displayed. 
To share your public key, choose option 3. To exit the program, choose option 4.

 
<h2>Security Notes and limitations:</h2>

* This project is for learning and demonstration purposes.

* Private keys currently exist only in memory for the duration of the program and are not persisted to disk. Saving keys to disk requires additional password based encryption of private files to keep them safe. 

* Base64 encoding in this program is used only for safely transporting the text (copy / paste), it is fully reversible by anyone and provides no cryptographic protection on its own.

<h2>Future Improvements:</h2>
Password protected private key storage  
File encryption mode  
Optional GUI  

<h2>Tech Stack:</h2>
Python 3  
Cryptography library  

