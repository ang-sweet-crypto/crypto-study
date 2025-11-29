from pwn import *
import hashlib
import itertools
import string
import re

# 1. 连接CTF题目服务器（替换成实际的IP/域名和端口）
io = remote("nc1.ctfplus.cn", 27031)

# 2. 接收服务器的proof of work提示
server_msg = io.recvline().decode().strip()
print(f"服务器提示: {server_msg}")

# 3. 从提示中提取「后缀」和「目标哈希」（用正则表达式匹配）
match = re.search(r'sha256\(XXXX\+(.*?)\) == (.*)', server_msg)
if not match:
    print("解析服务器提示失败！")
    io.close()
    exit()

suffix = match.group(1)       # 提取后缀（比如截图里的 v90dSzEdrbbEkB52PSx3WB1ulvO3）
target_hash = match.group(2)  # 提取目标哈希（比如截图里的 2a4cbc92367137f1cf1be82f04b56670a2f1a8625c323ffb11246930f57ce6db）
print(f"后缀: {suffix}")
print(f"目标哈希: {target_hash}")

# 4. 暴力破解4位前缀（XXXX）
chars = string.ascii_letters + string.digits  # 字符集：大小写字母+数字
found_prefix = None

# 枚举所有4位组合（共62^4种，电脑1~2秒能跑完）
for prefix_tuple in itertools.product(chars, repeat=4):
    test_prefix = ''.join(prefix_tuple)  # 把元组转成字符串（比如 ('a','B','3','z') → "aB3z"）
    test_str = test_prefix + suffix      # 拼接「前缀+后缀」
    # 计算SHA256哈希并比对
    if hashlib.sha256(test_str.encode()).hexdigest() == target_hash:
        found_prefix = test_prefix
        break

if not found_prefix:
    print("破解失败！可能字符集不对或服务器提示解析错误")
    io.close()
    exit()

print(f"破解成功！XXXX是: {found_prefix}")

# 5. 发送破解出的前缀给服务器
io.sendline(found_prefix)

# 6. 接收服务器的后续响应（比如flag或新的题目提示）
next_msg = io.recvline().decode().strip()
print(f"服务器后续响应: {next_msg}")

# 7. 进入手动交互模式（如果还需要进一步输入，比如和题目交互）
io.interactive()