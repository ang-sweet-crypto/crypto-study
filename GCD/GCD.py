def extended_gcd(a, b):
    # 自定义一个GCD函数
    old_r, r = a, b  # 上一步和当前的余数值（逗号隔开）
    old_s, s = 1, 0  # 上一步和当前的x的系数
    old_t, t = 0, 1  # 上一步和当前的y的系数

    # 当当前余数不为0时，循环计算（类似于辗转相除）
    while r != 0:
        # 计算商 = 上一步余数 ÷ 当前余数
        quotient = old_r // r

        # 下一步的"上一步余数"为当前余数
        # 下一步的“当前余数”为上一步余数-商×当前余数
        old_r, r = r, old_r - quotient * r

        # 更新x系数：原理同余数变化
        old_s, s = s, old_s - quotient * s

        # 更新y系数：同上
        old_t, t = t, old_t - quotient * t
    # 当余数r=0时，old_r就是gcd（即最后一个非零余数），old_s和old_t就是x和y
    return (old_r, old_s, old_t)

# 可替换的a,b值
a = 26513
b = 32321
# 调用自定义的GCD函数
gcd, x, y = extended_gcd(a, b)

print(f"{a}和{b}的最大公约数是：{gcd}")
print(f"满足 {a}×x + {b}×y = {gcd} 的解是：x={x}, y={y}")
print("验证：", a * x + b * y)  # 等于gcd及验证正确