import string
from binascii import unhexlify

# Hàm xor từng kí tự trong xâu 'str' với 'singlebyte'
def xor_byte(str, singlebyte):
  res = ''
  for c in str:
    res += bytes([c ^ singlebyte])
  return res.decode("utf-8")

data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded = unhexlify(data)

# Thử mọi single byte
for i in range(256):
    flag = (single_byte_xor(decoded, i))
    if "crypto{" in flag: # Một flag có dạng 'crypto{...' nên nếu có thì đây là flag
      print(flag)
      break
