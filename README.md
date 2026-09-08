<h1>Hybrid Encryption CLI</h1>
A command line tool for encrypting and decrypting messages using hybrid encryption which includes RSA and AES algorithms, with digital signature for authentication and integration.

<h2>Overview</h2>
This tool lets users encrypt and decrypt the message using the RSA and AES algorithm. The same encryption pattern used in TLS, HTTPS and SSH for secure encryption. The program uses AES to encrypt the text and then uses RSA to encrypt the AES public key. It was built as hands-on learning to understand how encryption schemes work under the hood instead of relying on a single library call.

<h2>Features:</h2>
-RSA-256 key pair generation
-AES-GCM for encrypting actual message
-RSA-OAEP encryption to securely wrapping the AES key
-RSA-PSS for authentication
-Base64 encoded output for copying, pasting and sharing as plain text
-Interactive command line manu to encrypt, decrypt and share your public key

<h2>Cryptographic decision:</h2>
Why hybrid instead of pure RSA?
RSA is well suited for key exchange but it’s not practical for encrypting the entire message directly. Its block size is limited by the key size( around 190 bytes for 2048 bit key) and its underlying modular exponentiation is comparatively more expensive than the symmetric encryption. Hybrid resolves both issues by dividing the work, AES handles the actual message since it's fast and has no meaningful size limit while RSA is used only to encrypt a small, fixed size AES key giving RSA key exchange security without compromising on its performance.
 
<h2>Why AES-256 over AES-128?</h2>
Both AES-256 and AES-128 are exceptionally secure and approved encryption standards but AES-256 uses larger keys and more processing rounds. However, the main reason for choosing AES-256 was to match the strength of RSA as RSA was using a 2048 bit key. So, both sides of hybrid encryption have similar strength in security. The extra computation cost of AES-256 over AES-128 is negligible at the scale of short text messages so added security comes with no real performance cost.
