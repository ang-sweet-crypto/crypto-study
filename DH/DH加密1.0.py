def dh_simulate(p, g, alice_a, bob_b):

    # 分别生成Alice和Bob的公钥
    alice_A = pow(g, alice_a, p)
    bob_B = pow(g, bob_b, p)

    # 分别计算Alice和Bob的共享密钥
    alice_shared = pow(bob_B, alice_a, p)
    bob_shared = pow(alice_A, bob_b, p)

    # 验证双方计算出的共享密钥是否一致
    # 若共享密钥不一致，说明可能遭受中间人攻击，模拟失败
    assert alice_shared == bob_shared
    return alice_shared

#手动输入p、g、alice_a、bob_b(可替换）
p = 23        # 模素数
g = 5         # 模素数p的本原根
alice_a = 6   # Alice的私钥
bob_b = 15    # Bob的私钥

shared_key = dh_simulate(p, g, alice_a, bob_b)
print(f"公共参数：p={p}, g={g}")
print(f"Alice的私钥：{alice_a}，公钥：{pow(g, alice_a, p)}")
print(f"Bob的私钥：{bob_b}，公钥：{pow(g, bob_b, p)}")
print(f"共享密钥：{shared_key}")
