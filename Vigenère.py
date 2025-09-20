def vigenere(plaintext, key):#定义维吉尼亚函数
    # 核心加密逻辑（只处理字母，忽略其他字符）
    result = []
    #储存加密后的字符（数字）
    key_length = len(key)
    #密钥的长度（方便后续循环使用）
    key_idx = 0
    #初始引索从0开始
    key = key.upper()  # 密钥统一转大写
    for c in plaintext:
        if c.isalpha():
            # 计算偏移：明文字母 + 密钥字母（A=0，Z=25）
            shift = ord(key[key_idx % len(key)]) - ord('A')
            # 处理大小写
            base = ord('A') if c.isupper() else ord('a')
            # 加密计算（模26确保在字母范围内）
            new_char = chr((ord(c) - base + shift) % 26 + base)
            result.append(new_char)
            key_idx += 1
        else:
            result.append(c)  # 非字母直接保留
    return ''.join(result)

# 最后三行可实现输入输出
plaintext = input("输入要加密的内容：")  # 输入p和k
key = input("输入密钥（字母）：")
print("加密结果：", vigenere(plaintext, key))  # 打印结果
