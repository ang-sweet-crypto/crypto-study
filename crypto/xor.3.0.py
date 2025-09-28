# 密文（十六进制字符串）
cipher_hex =  "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
# 密文转字节
cipher = bytes.fromhex(cipher_hex)
key = b"myXORkey"

# 解密：循环异或
flag = []
for i in range(len(cipher)):
    key_byte = key[i % len(key)]  # 循环取密钥字节
    plain_byte = cipher[i] ^ key_byte
    flag.append(chr(plain_byte))
# 拼接成 flag 格式
print("" + "".join(flag) + "")