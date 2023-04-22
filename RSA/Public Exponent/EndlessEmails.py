from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

def broadcast_attack(data):
  def extended_gcd(a, b):
    x, y = 0, 1
    lastx, lasty = 1, 0
    while b:
      a, (q, b) = b, divmod(a, b)
      x, lastx = lastx - q * x, x
      y, lasty = lasty - q * y, y
    return (lastx, lasty, a)
  def chinese_remainder_theorem(items):
    N = 1
    for a, n in items:
      N *= n
    result = 0
    for a, n in items:
      m = N // n
      r, s, d = extended_gcd(n, m)
      if d != 1:
        N = N // n
        continue
      result += a * s * m

    return result % N
  x = chinese_remainder_theorem(data)
  m = iroot(x, e)[0]
  return m

n = [n0, n1, n2, n3, n4, n5, n6]
c = [c0, c1, c2, c3, c4, c5, c6]
for i in range(5):
  for j in range(i + 1, 6):
      for k in range(j + 1, 7):
        data = [(c[i], n[i]), (c[j], n[j]), (c[k], n[k])]
        m = long_to_bytes(broadcast_attack(data))
        if b'crypto{' in m:
          print(i, j, k, )
          print(m.decode())
