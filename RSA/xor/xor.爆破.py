# 密文的十六进制字符串
hex_cipher = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# 十六进制转字节
cipher_bytes = bytes.fromhex(hex_cipher)

# 遍历所有可能的单字节密钥（0~255）
for key in range(256):
    # 对每个字节异或密钥，生成明文字节
    plain_bytes = bytes([b ^ key for b in cipher_bytes])
    try:
        # 尝试解码为ASCII（假设明文是ASCII文本）
        plain_text = plain_bytes.decode('ascii')
        # 检查是否为可打印的正常文本
        if plain_text.isprintable() and len(plain_text.strip()) > 0:
            print(f"找到密钥: {key} (十六进制: 0x{key:02x})")
            print(f"明文: {plain_text}")
    except UnicodeDecodeError:
        # 非ASCII可解码的情况，跳过
        continue