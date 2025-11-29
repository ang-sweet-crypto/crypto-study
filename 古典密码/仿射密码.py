def affine_encrypt(plaintext, k1, k0):
    ciphertext = ''
    for char in plaintext:

       if 'a' <= char <= 'z':
           m = ord(char) - ord('a')
           c = (k1 * m + k0) % 26
           encrypted_char = chr(c + ord('a'))
           ciphertext += encrypted_char
       else:
           ciphertext += char
    return ciphertext
if __name__ == '__main__':
    k1 = int(input('请输入k1:'))
    k0 = int(input('请输入k0:'))
    plaintext = input('请输入明文：')
    ciphertext = affine_encrypt(plaintext, k1, k0)
    print(f'加密结果为:{ciphertext}')


