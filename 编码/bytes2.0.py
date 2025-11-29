from Crypto.Util.number import long_to_bytes

number = 151470246090324385397502339491314847076012411468329635438482538829084452459

bytes_data = long_to_bytes(number)
print("字节数据（原始）:", bytes_data)  # 先查看字节内容

try:
    # 尝试 UTF-8 解码
    string_result = bytes_data.decode('utf-8')
    print("UTF-8 解码结果:", string_result)
except UnicodeDecodeError:
    print("UTF-8 解码失败，尝试 latin-1 解码（忽略错误）...")
    # 若不是文本，latin-1 可“强制”解码所有字节（适合二进制/任意字节）
    string_result = bytes_data.decode('latin-1', errors='ignore')
    print("latin-1 解码结果:", string_result)