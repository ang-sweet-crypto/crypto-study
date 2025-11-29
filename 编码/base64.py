import base64

encoded = "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"
decoded = base64.b64decode(encoded).decode('utf-8', errors='ignore')
print(decoded)