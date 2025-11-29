import sympy

def rsa_direct_factor(n, e, c, p=None, q=None):

    #用sympy分解小n
    if not p or not q:
        print("正在用sympy分解n...小n快，大n建议手动输p/q！")
        factors = sympy.factorint(n)  # RSA的n是两个素数乘积，所以factors长度必为2
        primes = list(factors.keys())
        if len(primes) != 2:
            raise ValueError("n不是两个素数乘积！不符合RSA标准，别瞎输参数啊！")
        p, q = primes[0], primes[1]

    # 验证分解是否正确
    assert p * q == n, f"分解错了！p*q={p * q}≠n={n}，再检查p和q！"

    # 算φ(n)和d，d是e的逆元
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)  # Python内置扩展欧几里得，比自己写的稳

    # 验证d对不对！e*d modφ(n)必须是1
    assert (e * d) % phi == 1, f"d算错了！e*d modφ(n)={(e * d) % phi}≠1"
    m = pow(c, d, n)
    return m, p, q, d

# 自定义测试参数（小n好验证，大n自己换）
n_test = 323
e_test = 65
c_test = 29

m_result, p_result, q_result, d_result = rsa_direct_factor(n_test, e_test, c_test)

# 输出结果，顺便验证m（m^e modn应该等于c）
print(f"解密成功！m={m_result}，p={p_result}，q={q_result}，d={d_result}")
assert pow(m_result, e_test, n_test) == c_test, "m错了！再检查exp！"
print(f"验证通过：m^e modn={pow(m_result, e_test, n_test)}=c={c_test}，太牛了！")