import string

def decrypt_vigenere(ciphertext, key):
    alphabet = string.digits + string.ascii_letters + string.punctuation
    alphabet_length = len(alphabet)

    key = [c for c in key if c in alphabet]
    key_length = len(key)
    plaintext = []
    key_idx = 0

    for c in ciphertext:
        if c in alphabet:
            c_pos = alphabet.index(c)
            key_pos = alphabet.index(key[key_idx % key_length])
            plain_pos = (c_pos - key_pos) % alphabet_length
            plaintext.append(alphabet[plain_pos])
            key_idx += 1
        else:
            plaintext.append(c)

    return ''.join(plaintext)

if __name__ == "__main__":
    ciphertext = input ("输入要解密的内容:")
    key = input("输入密钥:")

    try:
        result = decrypt_vigenere(ciphertext, key)
        print("解密结果：", result)
    except ValueError as e:
        print("错误：", str(e))
