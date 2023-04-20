from Crypto.Util.number import inverse
a = [2, 3, 5]
m = [5, 11, 17]
Gt = 1

for i in m:
  Gt *= i
  
M = [Gt // x for x in m]
y = [inverse(M[i], m[i]) for i in range(len(m))]
ans = 0

for i in range(len(m)):
  ans += a[i] * M[i] * y[i]
  
print(ans % Gt)
