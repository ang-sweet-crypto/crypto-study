p = 17
q = 19

n = p * q
phi = (p - 1) * (q - 1)
e = 7
d = 0
for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break

plaintext = 88
ciphertext = (plaintext ** e) % n
print(f"密文: {ciphertext}")

