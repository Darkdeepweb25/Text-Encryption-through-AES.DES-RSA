from Crypto.Cipher import DES
import base64

# Padding function for DES (block size is 8 bytes)
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Encrypt using DES
def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    encrypted_text = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted_text).decode()

# Decrypt using DES
def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(ciphertext)).decode().strip()
    return decrypted_text

# Main program
if __name__ == "__main__":
    print("=== DES Encryption Program ===")
    
    # Get user input
    key = input("Enter an 8-character key for DES: ").encode()
    if len(key) != 8:
        print("Error: Key must be exactly 8 characters.")
        exit()

    plaintext = input("Enter the text to encrypt: ")
    
    # Perform encryption
    encrypted_text = des_encrypt(key, plaintext)
    print(f"Encrypted text: {encrypted_text}")

    # Perform decryption
    decrypted_text = des_decrypt(key, encrypted_text)
    print(f"Decrypted text: {decrypted_text}")
