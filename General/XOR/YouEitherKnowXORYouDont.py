from binascii import unhexlify

# Hàm XOR 2 dãy bytes
def XOR(s1, s2):
  res = b''
  for a, b in zip(s1, s2):
    res += bytes([a ^ b])
  return res.decode("utf-8")

encoded = unhexlify('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
subencoded = encoded[0:7] # Lấy 7 kí tự của xâu Encoded
subflag = "crypto{".encode()
subSecretKey = XOR(subencoded, subflag) # Xor để được 7 kí tự của SecretKey: "myXORke"
subSecretKey = (subSecretKey + 'y').encode() # Ta đoán được rằng là "myXORkey", sau đó giải mã để thực hiện XOR

lenEncoded = len(encoded) # Độ dài xâu Encoded
lenSecretKey = 7 # Độ dài hiện tại của SecretKey

# Nhân đôi subSecretKey cho đến khi có độ dài lớn hoặc bằng với Encoded
while lenSecretKey < lenEncoded:
  lenSecretKey *= 2
  subSecretKey += subSecretKey

secretKey = subSecretKey[:lenEncoded] # SecretKey có độ dài bằng với Encoded
print(XOR(secretKey, encoded))
