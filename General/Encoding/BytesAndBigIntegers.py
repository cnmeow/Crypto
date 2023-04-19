!pip3 install PyCryptodome # Cài đặt thư viện PyCryptodome
from Crypto.Util.number import long_to_bytes
longnum = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# Chuyển long thành bytes để lấy flag
flag = long_to_bytes(longnum)
print(flag)
