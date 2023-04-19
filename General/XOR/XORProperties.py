from binascii import unhexlify

# Hàm XOR 2 xâu kí tự
def XOR(s1, s2):
  res = ''
  for a,b in zip(s1, s2):
    res += format(int(a, 16) ^ int(b, 16), 'x')
  return res

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e" # KEY2 ^ KEY1
KEY2_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1" # KEY2 ^ KEY3
FLAG_KEY1_KEY3_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" # FLAG ^ KEY1 ^ KEY3 ^ KEY2

KEY2 = XOR(KEY1, KEY2_KEY1) # KEY2 = KEY1 ^ (KEY2 ^ KEY1)
KEY3 = XOR(KEY2, KEY2_KEY3) # KEY3 = KEY2 ^ (KEY2 ^ KEY3)
FLAG = XOR(FLAG_KEY1_KEY3_KEY2, XOR(KEY1, XOR(KEY2, KEY3))) # FLAG = (FLAG ^ KEY1 ^ KEY3 ^ KEY2) ^ (KEY1 ^ (KEY2 ^ KEY3))

# Giải mã Hex sang kí tự
print(unhexlify(FLAG))
