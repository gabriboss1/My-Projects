# E2EE Messaging App

10/30/2024


I wanted to make a messaging application similar to WhatsApp, where messages are end-to-end encrypted to assure privacy.

In this code messages are encrypted and decrypted on the client end they pass through the server to be sent to other clients. The code uses 20-digit prime numbers for the encryption and decryption of messages, to make the unscrambling of messages during eventual interceptions much more challenging.

I'm very proud of the end-to-end nature of the encryption, which was tough to implement due to socket buffer sizes, messages sending in chunks, and integer size being too large for conversions. The next step in this project would be to implement a UI. 
