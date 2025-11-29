str=input("请输入明文：")
n=int(input("请输入密钥："))
str_encrypt=""
for letter in str:
    if "a"<=letter<="z":
        str_encrypt +=chr((ord(letter)-ord("a") +n) %26 +ord("a"))
    elif "A"<=letter<="Z":
        str_encrypt +=chr((ord(letter)-ord("A") +n) %26 +ord("A"))
    else:
        str_encrypt += letter
print("密文为：",str_encrypt)

str=input("请输入密文：")
n=int(input("请输入密钥："))
str_decrypt=""
for word in str:
    if "a"<=word<="z":
        str_decrypt +=chr((ord(word)-ord("a") -n) %26 +ord("a"))
    elif "A"<=word<="Z":
        str_decrypt +=chr((ord(word)-ord("A") -n) %26 +ord("A"))
    else:
        str_decrypt += word
print("明文为：",str_decrypt)