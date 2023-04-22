import requests
from Crypto.Util.number import long_to_bytes

# Nhận ciphertext
r = requests.get('http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag')
res = r.json()['ciphertext']
iv = res[:32]

flag = ""

# Giải mã flag
for i in range(1,3):
    cipher = res[32*i:32*(i+1)]
    plain = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher)
    resp = plain.json()['plaintext']
    res1 = hex(int(resp,16) ^ int(iv, 16))[2:]
    flag = flag + res1
    iv = cipher

print(long_to_bytes(int(flag, 16)))
