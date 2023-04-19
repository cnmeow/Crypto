import math
num = 13
multi = 1

# Để 3*d ≡ 1 mod 13 thì 3*d = (1 số là bội của 13) + 1
# Tìm bội của 13 mà (bội + 1) chia hết cho 3
while (num + 1) % 3 != 0:
  num *= multi
  multi += 1

print(int((num + 1)/3))
