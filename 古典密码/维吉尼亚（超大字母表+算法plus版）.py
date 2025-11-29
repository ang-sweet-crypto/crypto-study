from string import digits, ascii_letters, punctuation, ascii_lowercase

alphabet = digits + ascii_letters + punctuation
key = "QAQ(@.@)"
ciphertext = "0l0CSoYM<c;amo_P_"
prefix = "0xGame{"

key_offsets = [alphabet.index(c) for c in key]
m = len(alphabet)
result = []

for i, c in enumerate(ciphertext):
    c_pos = alphabet.index(c)
    bias = key_offsets[i % len(key_offsets)]

    for x in range(m):
        if (x + bias) * x % m == c_pos:
            char = alphabet[x]

            if i < len(prefix) and char == prefix[i]:
                result.append(char)
                break
            elif i == len(ciphertext) - 1 and char == "}":
                result.append(char)
                break
            elif i >= len(prefix) and i < len(ciphertext) - 1 and char in ascii_lowercase:
                result.append(char)
                break

print(''.join(result))
