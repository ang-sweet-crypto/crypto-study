import hashlib

# 目标MD5值
target_md5 = "a7653b26825c5a142db0b7c53fe7091a"

# 遍历所有四位数字（0000 ~ 9999）
for num in range(10000):
    # 格式化为4位字符串（不足4位补前导零，如12 → "0012"）
    four_digit = f"{num:04d}"
    # 拼接成目标格式字符串："四位数字crypto"
    text = four_digit + "crypto"
    # 计算MD5（需先将字符串编码为bytes）
    md5_result = hashlib.md5(text.encode()).hexdigest()
    # 比对MD5
    if md5_result == target_md5:
        print(f"匹配成功！字符串为：{text}")
        break
else:
    print("未找到匹配的字符串")