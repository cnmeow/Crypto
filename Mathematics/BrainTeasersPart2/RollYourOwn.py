from sympy.ntheory.residue_ntheory import discrete_log
from Crypto.Util.Padding import unpad
from json import loads, dumps
from Crypto.Cipher import AES
from hashlib import sha1
import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 13403

tn = telnetlib.Telnet(HOST, PORT)

def decrypt_flag(shared_secret, iv, ciphertext):
    key = sha1(str(shared_secret).encode()).digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    plaintext = AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext)
    return unpad(plaintext, 16).decode()

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

print(tn.read_until(b': "'))
q = readline()[:-2]
q = int(q, 16)
data = {
    "g": hex(q+1), 
    "n": hex(q**2)
}
json_send(data)
print(tn.read_until(b'public key: "'))
publickey = readline()[:-2]
publickey = int(publickey, 16)
data = {
    "x": hex((publickey-1)//q)
}
json_send(data)
print(tn.read_until(b' private key: '))
print(json_recv()["flag"])
