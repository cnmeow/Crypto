from gmpy2 import invert
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
print(invert(e, (p - 1) * (q - 1)))