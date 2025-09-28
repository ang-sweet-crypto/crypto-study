# 第一步：指定两个质数
p = 17
q = 19

# 第二步：计算n = p * q（n同时是公钥、密钥的一部分）
n = p * q
# 第三步：计算欧拉函数φ(n) = (p-1)*(q-1)
phi = (p - 1) * (q - 1)
# 第四步：指定一个整数e使其与phi互质，并由e组成公钥的一部分
e = 7
# 第五步：计算d，使得(e*d) mod phi = 1，并由d组成私钥的一部分
d = 0
for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break

ciphertext = 8953232 # 输入密文
# 解密：明文 = (密文^d) mod n
decrypted_text = (ciphertext ** d) % n
print(f"明文: {decrypted_text}")
