from binascii import unhexlify
import base64
# Giải mã hex sang bytes
bytes = unhexlify('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')
# Mã hóa nó sang Base64
flag = base64.b64encode(bytes)
print(flag)
