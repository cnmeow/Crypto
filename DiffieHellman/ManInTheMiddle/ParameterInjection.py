"""
#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 13371

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

tn.read_until(b"Alice: ")
data = json_recv()
p, g, A = int(data["p"], 16), int(data["g"], 16), int(data["A"], 16)
sendBob = {
    "p": "0x01",
    "g": "0x01",
    "A": "0x01"
}
json_send(sendBob)
tn.read_until(b"Bob: ")
readline()
sendAlice = {
    "B":"0x01"
}
json_send(sendAlice)
print(readline()) 
> b'Send to Alice: Intercepted from Alice: {"iv": "f93e22fd2dcaeb6276fd02fa71b3e3f5", "encrypted_flag": "4c27b1aa9d02ed3c3b5614d7c5fab74dcd302a75ad017633abc29cdff3d4136e"}\n'
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

shared_secret = 1
iv = '5dc0f6b8f35bbf25d82505f16b9ebc8d'
ciphertext = 'f888867b7260f4bdc1be2cf349e9a8220a70342fc4ac8f3e21f27fa6fb915f4d'

print(decrypt_flag(shared_secret, iv, ciphertext))
