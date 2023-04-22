import requests
import hashlib
from Crypto.Cipher import AES

# Nhận encrypted flag
r = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
res = bytes.fromhex(r.json()['ciphertext'])

# Thử mọi keyword trong file word
with open('/content/words.txt', 'r') as f:
    for words in f:
        words = words.strip()
        key = hashlib.md5(words.encode()).digest()
        
        # Gửi đến server để nhận cipher
        cipher = AES.new(key, AES.MODE_ECB)
        
        res1 = cipher.decrypt(res)
        if res1.startswith('crypto{'.encode()):
            print(res1)
            break
