def rail_encrypt(text, rails):
    # 初始化对应栏数的空列表
    fence = [''] * rails
    rail, dir = 0, 1  # rail=当前栏号，dir=方向(1下/-1上)
    for c in text:
        fence[rail] += c  # 字符放入当前栏
        # 触顶/触底时改变方向
        if rail == 0:
            dir = 1
        elif rail == rails - 1:
            dir = -1
        rail += dir  # 移动到下一栏
    return ''.join(fence)  # 拼接所有栏的字符

text = input("输入要加密的内容：")
rails = int(input("输入栏数（数字）："))
print("加密结果：", rail_encrypt(text, rails))
