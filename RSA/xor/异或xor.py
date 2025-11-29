s = "label"
key = 13
new_string = ''.join(chr(ord(c) ^ key) for c in s)
print(f"crypto{{{new_string}}}")