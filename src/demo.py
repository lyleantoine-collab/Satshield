import base64  # Simple encrypt tool

def encrypt_signal(data):
    return base64.b64encode(data.encode())

def decrypt_signal(encoded):
    return base64.b64decode(encoded).decode()

# Test it
message = "Hello from Satshield!"
encrypted = encrypt_signal(message)
print("Encrypted:", encrypted)
decrypted = decrypt_signal(encrypted)
print("Back to normal:", decrypted)
