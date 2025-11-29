from Crypto.Util.number import *
from base64 import b64decode

c0 = b'MHhHYW1le7u2063AtLW9MHhHYW1lMjAyNQ=='
c1 = "a3accfd6d4dac4e3d2d1beadd1a7bbe143727970746fb5c4bb"
c2 = "wqwwwqqaawwwaaqawqwawwwwaaawwwawaqqwwwqaqwwqwaaqwaqqaaawqqqaqaqwaaawwwqaqaaaaqawaqqqwwqqwaqwqwwwawawqqwwqqawqwaqwwawwqwaqqaqwaw"
c3 = 5787980659359196741038715872684190805073807486263453249083702093905274294594502252203577660251756609738877887210677202141957646934092054500618364441642896304387589669635034683021946777034215355675802286923927161922717560413551789421376288823912349463080999424773600185557948875343480056576969695671340947861706467351885610345887785319870159654836532664189086047061137903149197973327299859185905186913896041309284477616128

part0 = b64decode(c0)
part1 = bytes.fromhex(c1)

# 解密c2：三进制映射反转
def decrypt_c2(s):
    mapper = {'a':0, 'w':1, 'q':2}  # 反向映射
    reversed_s = s[::-1]  # 反转字符串（加密时是从低位开始拼接的）
    num = 0
    for c in reversed_s:
        num = num * 3 + mapper[c]  # 还原三进制数
    # 转换为25字节（因为flag分4份，每份25字节）
    return num.to_bytes(25, byteorder='big', signed=False)

part2 = decrypt_c2(c2)

def decrypt_c3(n):
    # 二分法查找7次方根（避免浮点数溢出）
    left, right = 0, n  # 左边界0，右边界初始设为n（因为root⁷=n → root≤n）
    root = 0
    while left <= right:
        mid = (left + right) // 2
        try:
            power = mid ** 7  # 尝试计算mid的7次方
        except OverflowError:
            power = float('inf')  # 溢出时视为“极大值”，说明mid过大
        if power == n:
            root = mid
            break
        elif power < n:
            left = mid + 1  # mid的7次方太小，增大左边界
        else:
            right = mid - 1  # mid的7次方太大，减小右边界
    # 小端序转25字节
    return root.to_bytes(25, byteorder='little', signed=False)

part3 = decrypt_c3(c3)

# 拼接4部分，提取原始flag（去掉填充的随机字节）
full_flag = part0 + part1 + part2 + part3
# 原始flag是gb2312编码，且长度小于100，取前半部分有效内容
flag = full_flag.split(b'\x00')[0].decode('gb2312', errors='ignore')  # 忽略无效字符
print("解密得到的flag：", flag)