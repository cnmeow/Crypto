flag = 30

# Tìm số x sao cho (dư lượng bậc 2 modulo cho 29) là 1 số nằm trong mảng đề cho
for num in [14, 6, 11]:
  for x in range(29):
    if pow(x, 2, 29) == num:
      flag = min(flag, x) # Tìm số nhỏ nhất
print(flag)
