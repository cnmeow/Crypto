"""
Chạy code sau để nhận dữ liệu từ server
from sympy.ntheory.residue_ntheory import discrete_log
from Crypto.Util.Padding import unpad
from json import loads, dumps
from Crypto.Cipher import AES
from hashlib import sha1
import telnetlib
import json 

HOST = "socket.cryptohack.org"
PORT = 13380

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

print(readline())
print(readline())
print(readline())

>b'Intercepted from Alice: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x1094e97e5d039d2673ac579ac01e1826f905afe5a903c1984217bd0433b3dd8d0c36aa058308f32b23d2ca004f463caec0911d1695eec115fa6efc349c554bbe938b26a080503084280559efe7ee7fe4e68f5c935662f422183a543d509c3eea90709017cb8d335b3c70508c0323897fb726ae39b61ef575520a659a5f725e2c520ceeddbaddfdf5f551f5f44c32b3db10680a1c8b8fef2f85b65b8fa5e6282e86ad9894c2e28509be94b752f552d0b4c6c8a7e5b645144ecd804dde38cd2fac"}\n'
>b'Intercepted from Bob: {"B": "0xc827bf107985a82a2a2a031ccedaea65d911678f12a27c92e51643b9701a7113eedbb62093193d529dfa1f7e7d9b224dc27b4d48fab03908476c750dbf4be0cb43a1623afe9e55c0a8870fc94a71ba11fac552338bb72e2ad4c19161a11d9c7ec1ee906b80c0de695d677716870dbc731b716cfec4c468dae7be06e8c03657055ca7a4ccc7fd8e76713bdfecc33bfcd26c9702b74ddd2140f0a9d672247b1bad07dc387fb4654ea2af496c42c13f24780931ec7c5c46b190eae748a615a34cf3"}\n'
>b'Intercepted from Alice: {"iv": "6ad3b8fb367ee88d02b1b245e765de60", "encrypted": "82045cb145549377f7bedf0676f8068b6f0f9d548c7ec8cbf52a7b53bd1db217a0efe2a8bd11316aef98a154acfb3c87"}\n'
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Util.number import inverse

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

p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 0x02
A = 0x1094e97e5d039d2673ac579ac01e1826f905afe5a903c1984217bd0433b3dd8d0c36aa058308f32b23d2ca004f463caec0911d1695eec115fa6efc349c554bbe938b26a080503084280559efe7ee7fe4e68f5c935662f422183a543d509c3eea90709017cb8d335b3c70508c0323897fb726ae39b61ef575520a659a5f725e2c520ceeddbaddfdf5f551f5f44c32b3db10680a1c8b8fef2f85b65b8fa5e6282e86ad9894c2e28509be94b752f552d0b4c6c8a7e5b645144ecd804dde38cd2fac
B = 0xc827bf107985a82a2a2a031ccedaea65d911678f12a27c92e51643b9701a7113eedbb62093193d529dfa1f7e7d9b224dc27b4d48fab03908476c750dbf4be0cb43a1623afe9e55c0a8870fc94a71ba11fac552338bb72e2ad4c19161a11d9c7ec1ee906b80c0de695d677716870dbc731b716cfec4c468dae7be06e8c03657055ca7a4ccc7fd8e76713bdfecc33bfcd26c9702b74ddd2140f0a9d672247b1bad07dc387fb4654ea2af496c42c13f24780931ec7c5c46b190eae748a615a34cf3
iv = "6ad3b8fb367ee88d02b1b245e765de60"
encrypted = "82045cb145549377f7bedf0676f8068b6f0f9d548c7ec8cbf52a7b53bd1db217a0efe2a8bd11316aef98a154acfb3c87"
a = A * inverse(g, p)
shared_secret = (a * B) % p
print(decrypt_flag(shared_secret, iv, encrypted))
