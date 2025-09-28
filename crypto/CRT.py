#用扩展欧几里得算法求gcd和逆元
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

# 实现普通CRT（注意：模数两两互素）
def crt(remainders, moduli):
    current_sol = 0  # 跟踪当前合并后的解（初始解：x ≡ 0 mod 1）
    current_mod = 1  # 跟踪当前合并后的模数（初始模数：1）

    # 遍历每个同余方程：x ≡ a (mod m)
    for a, m in zip(remainders, moduli):
        # 用扩展欧几里得求当前模数current_mod在模m下的逆元
        gcd, inv, _ = extended_gcd(current_mod, m)

        # 普通CRT要求模数互素（gcd必须为1），否则无解
        if gcd != 1:
            return "错误：模数不互素，普通CRT无法求解"

        # 解同余方程：current_sol + k*current_mod ≡ a (mod m)
        # 转化为求k：k ≡ (a - current_sol) * 逆元 (mod m)
        k = ((a - current_sol) * inv) % m

        # 更新当前解和当前模数
        current_sol += k * current_mod  # 新解 = 旧解 + k×旧模数
        current_mod *= m  # 新模数 = 旧模数 × 当前模数（因互素）

        # 取模让解保持最小（避免数值过大）
        current_sol %= current_mod

    return current_sol

# 解方程组（可替换为多组互素的数，这里只列举出两组的情况）
if __name__ == "__main__":
    remainders = [2, 5]
    moduli = [3, 10]
    solution = crt(remainders, moduli)
    print(f"方程组的解：{solution}")
    print(f"验证：{solution} mod 3 = {solution % 3}（应等于2）")
    print(f"验证：{solution} mod 10 = {solution % 10}（应等于5）")

