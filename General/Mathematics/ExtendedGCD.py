import math

p = 26513
q = 32321
gcd = 1 # Ước chung lớn nhất của p và q (2 số nguyên tố) là 1
u = 0

# Tìm cho đến khi thấy u, v
while 1:
  v = gcd - u*p
  if v % q == 0: # Nếu v là số nguyên
    print(int(min(u, v/q))) # Xuất ra số nhỏ nhất giữa u và v
    break
  else: u = u+1
