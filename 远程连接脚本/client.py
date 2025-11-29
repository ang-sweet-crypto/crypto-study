import socket

# 容器地址和端口（平台提供：challenge.ctfplus.cn:33887）
CONTAINER_HOST = "nc nc1.ctfplus.cn"
CONTAINER_PORT = 20643

# 创建 TCP 客户端并连接容器
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((CONTAINER_HOST, CONTAINER_PORT))

# 1. 接收服务端发送的密文提示
data = client.recv(1024).decode()
print("服务端（容器）发来的消息：\n", data)

# 2. 发送 MD5 碰撞对（使用经典碰撞样本）
input1 = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bddd"
input2 = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bddd"
client.send(f"{input1},{input2}".encode())

# 3. 接收服务端返回的密钥（key）
response = client.recv(1024).decode()
print("服务端（容器）返回的 key：\n", response)  # 记录下 key（如 "The key is: xxxxxx"）

client.close()