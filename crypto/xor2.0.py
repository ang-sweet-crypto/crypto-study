# 1. 定义已知的十六进制字符串
KEY1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_XOR_ALL_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# 2. 工具函数：十六进制字符串转字节数组
def hex2bytes(hex_str):
    return bytes.fromhex(hex_str)

# 3. 工具函数：两个字节数组逐字节异或
def xor_bytes(a, b):
    assert len(a) == len(b), "异或的两个字节数组长度必须一致"
    return bytes([x ^ y for x, y in zip(a, b)])

# 4. 计算 KEY1 ^ KEY2 ^ KEY3 = KEY1 ^ (KEY2 ^ KEY3)
A = xor_bytes(hex2bytes(KEY1_hex), hex2bytes(KEY2_XOR_KEY3_hex))

# 5. 计算 FLAG = (FLAG ^ KEY1^KEY2^KEY3) ^ (KEY1^KEY2^KEY3)
FLAG_bytes = xor_bytes(hex2bytes(FLAG_XOR_ALL_hex), A)

# 6. 字节数组转十六进制字符串（FLAG的十六进制形式）
FLAG_hex = FLAG_bytes.hex()

# 7. （可选）十六进制转ASCII（得到人类可读的FLAG）
FLAG_ascii = FLAG_bytes.decode("ascii")

# 输出结果
print("FLAG的十六进制形式：", FLAG_hex)
print("FLAG的ASCII形式（最终答案）：", FLAG_ascii)