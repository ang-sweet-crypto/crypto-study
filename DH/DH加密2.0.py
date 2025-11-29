from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# ===================== 步骤1：生成RSA密钥对（用于身份签名） =====================
# Alice的RSA密钥对
alice_rsa_private = rsa.generate_private_key(
    public_exponent=65537,  # 公钥指数，常规选65537
    key_size=2048           # 密钥长度，越长越安全
)
alice_rsa_public = alice_rsa_private.public_key()

# Bob的RSA密钥对
bob_rsa_private = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
bob_rsa_public = bob_rsa_private.public_key()

# ===================== 步骤2：DH参数与密钥生成 =====================
# DH公共参数（实际应用需选大素数和本原根）
p = 23        # 示例用小素数，方便手动验证
g = 5         # 模23的本原根（5的幂能生成1~22所有数）

# Alice的DH私钥 + 公钥
alice_dh_private = 6
alice_dh_public = pow(g, alice_dh_private, p)  # 计算 g^a mod p

# Bob的DH私钥 + 公钥
bob_dh_private = 15
bob_dh_public = pow(g, bob_dh_private, p)     # 计算 g^b mod p

# ===================== 步骤3：对“身份+DH公钥”进行RSA签名 =====================
# Alice签名自己的“身份+DH公钥”
alice_identity = b"Alice"  # 身份标识
alice_sign_data = alice_identity + str(alice_dh_public).encode()  # 待签名数据
alice_signature = alice_rsa_private.sign(
    alice_sign_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),  # 掩码生成函数
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()  # 哈希算法
)

# Bob签名自己的“身份+DH公钥”
bob_identity = b"Bob"
bob_sign_data = bob_identity + str(bob_dh_public).encode()
bob_signature = bob_rsa_private.sign(
    bob_sign_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# ===================== 步骤4：验证对方签名（防止中间人） =====================
# Alice验证Bob的签名
try:
    bob_rsa_public.verify(
        bob_signature,
        bob_sign_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Alice验证Bob的签名成功 → Bob的DH公钥可信，无中间人攻击。")
except InvalidSignature:
    print("Alice验证Bob的签名失败 → 存在中间人攻击风险！")

# Bob验证Alice的签名
try:
    alice_rsa_public.verify(
        alice_signature,
        alice_sign_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Bob验证Alice的签名成功 → Alice的DH公钥可信，无中间人攻击。")
except InvalidSignature:
    print("Bob验证Alice的签名失败 → 存在中间人攻击风险！")

# ===================== 步骤5：计算共享密钥（验证通过后） =====================
alice_shared = pow(bob_dh_public, alice_dh_private, p)  # 计算 (g^b)^a mod p
bob_shared = pow(alice_dh_public, bob_dh_private, p)    # 计算 (g^a)^b mod p

print(f"\nAlice 计算的共享密钥：{alice_shared}")
print(f"Bob 计算的共享密钥：{bob_shared}")
assert alice_shared == bob_shared, "DH共享密钥不一致，流程错误！"
print("验证通过：Alice与Bob的共享密钥一致。")