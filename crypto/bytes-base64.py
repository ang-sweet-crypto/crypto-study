import base64

# 可替换的十六进制字符串
hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# 1. 十六进制解码为字节
bytes_data = bytes.fromhex(hex_string)

# 2. 字节编码为 Base64（再用 .decode('ascii') 转成字符串形式）
base64_result = base64.b64encode(bytes_data).decode('ascii')

print(base64_result)