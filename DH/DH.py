from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib

enc_hex = "be4df6ec7041494239db7d9c7b8e016dfe6b9ed474247104d18420cfc70145745c8b13d29998edcef0e2ed79cae558ca"
enc_bytes = bytes.fromhex(enc_hex)  # 将十六进制密文转换为字节，便于AES计算

# 计算AES密钥：s=1 → 转换为字节后做SHA256哈希
s = 1
key = hashlib.sha256(long_to_bytes(s)).digest()

# 创建AES-ECB解密器并解密
cipher = AES.new(key, AES.MODE_ECB)
decrypted = cipher.decrypt(enc_bytes)

# 输出解密结果（去除可能的填充后即为flag）
print(decrypted.strip())