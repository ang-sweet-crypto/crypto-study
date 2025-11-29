def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return (old_r, old_s, old_t)


def general_crt(remainders, moduli):
    current_a = 0  # 当前的解的余数
    current_m = 1  # 当前的模数

    # 逐个合并每个方程
    for a, m in zip(remainders, moduli):
        # 用扩展欧几里得求current_m和m的最大公约数，以及系数
        gcd, x, y = extended_gcd(current_m, m)

        # 检查是否有解：(a - current_a)必须能被gcd整除
        if (a - current_a) % gcd != 0:
            return f"无解：方程 x≡{current_a}({current_m}) 和 x≡{a}({m}) 矛盾"

        # 计算新的模数（最小公倍数 = 两数乘积 ÷ 最大公约数）
        lcm = current_m // gcd * m

        # 计算合并后的新余数（解）
        # 先求系数k的最小正整数解
        k = ((a - current_a) // gcd * x) % (m // gcd)
        # 新的解 = 原来的解 + k×原来的模数
        new_a = current_a + k * current_m

        # 取模让解变小
        current_a = new_a % lcm
        current_m = lcm

    return current_a  # 返回最小正整数解


if __name__ == "__main__":
#求解三个方程组
    remainders = [2, 3, 5]
    moduli = [5, 11, 17]
    solution = general_crt(remainders, moduli)
    print(f"\n解：{solution}")

    if isinstance(solution, int):  # 如果有解才验证
        print(f"验证：{solution} mod 5 = {solution % 5}（应等于2）")
        print(f"验证：{solution} mod 11 = {solution % 11}（应等于3）")
        print(f"验证：{solution} mod 17 = {solution % 17}（应等于5）")
