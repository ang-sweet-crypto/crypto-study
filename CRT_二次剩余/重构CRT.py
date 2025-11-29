from sympy.ntheory.modular import crt
from Crypto.Util.number import long_to_bytes
from sympy import primerange

primes = list(primerange(2, 114514))

c = [1, 2, 2, 4, 0, 2, 11, 11, 8, 23, 1, 30, 35, 0, 18, 30, 55, 60, 29, 42, 8, 13, 49, 11, 69, 26, 8, 73, 84, 67, 100, 9, 77, 72, 127, 49, 57, 74, 70, 129, 146, 45, 35, 180, 196, 101, 100, 146, 100, 194, 2, 161, 35, 155]

# 确定对应的模数（素数）：第一个素数是2，后续是primes[1]到primes[53]（共54个）
moduli = [2] + primes[1:54]  # 因为c有54个元素，所以需要54个模数
# 应用CRT求解原始整数message_int
# crt函数返回 (解, 模数乘积)，这道题只需要解
reconstructed, _ = crt(moduli, c)

flag = long_to_bytes(reconstructed).decode()
print("还原的flag:", flag)