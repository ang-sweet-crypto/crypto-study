from Crypto.Util.number import long_to_bytes

number = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
# 将整数转换为字节
bytes_data = long_to_bytes(number)
# 将字节解码为字符串（用 utf-8 编码，根据实际情况调整）
string_result = bytes_data.decode('utf-8')

print("转换后的字符：", string_result)  # 输出结果