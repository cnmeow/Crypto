import base64 # Để giải mã base64 
import codecs # Đẻ giải mã rot13
from Crypto.Util.number import long_to_bytes # Để giải mã bigint

import telnetlib
import json

# Kết nối đến server
HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

# Hàm đọc dữ liệu từ server
def readline():
    return tn.read_until(b"\n")

# Hàm chuyển dữ liệu từ server thành json
def json_recv():
    line = readline()
    return json.loads(line.decode())

# Hàm gửi dữ liệu đến server
def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

# Hàm giải mã 'encoded' có kiểu mã hóa là 'type'
def decoder(type, encoded):
    # Giải mã base64
    if type == 'base64':
        return base64.b64decode(encoded).decode()
    # Giải mã hex
    elif type == 'hex':
        return bytes.fromhex(encoded).decode('utf-8')
    # Giải mã rot13
    elif type == 'rot13':
        return codecs.decode(encoded, "rot13")
    # Giải mã bigint
    elif type == 'bigint':
        return long_to_bytes(int(encoded, 16)).decode()
    # Giải mã utf-8
    elif type == 'utf-8':
        flag = ""
        for c in encoded:
            flag += chr(c)
        return flag
      
# Nhận 100 dữ liệu bị mã hóa từ server, giải mã chúng rồi gửi lại đến server
for i in range (1, 101):
    received = json_recv() # Nhận dữ liệu từ server
    type = received["type"] 
    flag = received["encoded"]  
    flag = decoder(type, flag) # Giải mã
    to_send = {
        "decoded": flag
    }
    json_send(to_send) # Gửi mã đã giải cho server

# Sau khi giải mã xong 100 dữ liệu, ta thu được flag
print(json_recv())
