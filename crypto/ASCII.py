def ascii_to_string(ascii_codes):
    """
    将ASCII编码值转换为字符串
    参数:
        ascii_codes: 可以是整数列表（如[72, 101, 108]）或包含数字的字符串（如"72 101 108"）
    返回:
        转换后的字符串
    """
    # 处理输入为字符串的情况
    if isinstance(ascii_codes, str):
        # 分割字符串并转换为整数列表
        ascii_codes = list(map(int, ascii_codes.split()))

    # 验证每个值是否在ASCII范围内（0-127）
    for code in ascii_codes:
        if not (0 <= code <= 127):
            raise ValueError(f"值 {code} 超出ASCII编码范围（0-127）")

    # 将每个ASCII码转换为字符并拼接
    return ''.join(chr(code) for code in ascii_codes)

# 两种不同的用法，使用时按需求替换密文即可
if __name__ == "__main__":
    # 用法一：密文为整数列表
    ascii_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    result1 = ascii_to_string(ascii_list)
    print("示例1结果:", result1)  # 输出: Hello, World!

    # 用法二：密文为空格分隔的数字字符串
    ascii_str = "65 66 67 97 98 99 48 49 50"
    result2 = ascii_to_string(ascii_str)
    print("示例2结果:", result2)  # 输出: ABCabc012
