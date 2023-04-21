"""
Chạy code sau để kết nối server và lấy giá trị cần thiết
#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 13379

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

print(readline())
send1 = {"supported":["DH64"]}
json_send(send1)
print(readline())
send2 = {"chosen":"DH64"}
json_send(send2)
print(readline())
print(readline())
print(readline())

>b'Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}\n'
>b'Send to Bob: Intercepted from Bob: {"chosen": "DH64"}\n'
>b'Send to Alice: 
>Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x637430f37c694fa7"}
>Intercepted from Bob: {"B": "0x7249365a2a8c71ff"}                                                                                                                       
>Intercepted from Alice: {"iv": "31077c28f19c90297f3da6dff6ca3019", "encrypted_flag": "0ebb53dab97122361cfa8cdbb5ddc092a5af41452aae8def0d27181b6ee89839"}

"""
from Crypto.Cipher import AES
from Crypto.Util import number
import hashlib

p = int("0xde26ab651b92a129", 16)
g = int("0x2", 16)
A = int("0x637430f37c694fa7", 16)
B = int("0x7249365a2a8c71ff", 16)
iv =  "31077c28f19c90297f3da6dff6ca3019"
encrypted_flag = "0ebb53dab97122361cfa8cdbb5ddc092a5af41452aae8def0d27181b6ee89839"
iv = bytes.fromhex(iv)
encrypted_flag = bytes.fromhex(encrypted_flag)

def decrypt(secret, iv, cipher):
    sha1 = hashlib.sha1()
    sha1.update(str(secret).encode())
    key = sha1.digest()[:16]
    aes = AES.new(key, AES.MODE_CBC, iv)
    plain = aes.decrypt(cipher)
    print(plain)

a = 7596561454821291306 # Vào web ‘https://www.alpertron.com.ar/DILOG.HTM’ để tính Secretkey của Alice: a = DiscreteLog(Base = g, Power = A, Modulus = p)
shared_secret = pow(B, a, p)
decrypt(shared_secret, iv, encrypted_flag)
