prime = [853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997] # Các số nguyên tố có 3 chữ số
m = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
flag = True
for p in prime:
  for x in range(2, 1000):
    for i in range(len(m) - 1):
      if m[i] * x % p == m[i + 1]: flag = True
      else: 
        flag = False
        break
    if flag:
      print(p, x)
      break
  if flag: break
