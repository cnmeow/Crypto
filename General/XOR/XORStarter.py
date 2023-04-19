data = "label"
flag = ''

# Lấy từng kí tự "label" xor cho 13, chuyển nó thành kí tự rồi nối vào flag
for c in data:
    flag += chr(ord(c) ^ 13)

print("crypto{"+flag+"}")
