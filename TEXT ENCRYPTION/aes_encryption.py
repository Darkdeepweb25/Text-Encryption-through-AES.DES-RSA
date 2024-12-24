from Crypto.Cipher import AES
import base64

# Function to pad the plaintext to make it a multiple of 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Function to encrypt text
def encrypt_text(key, plaintext):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    return nonce, base64.b64encode(ciphertext).decode()

# Function to decrypt text
def decrypt_text(key, nonce, ciphertext):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_text = cipher.decrypt(base64.b64decode(ciphertext)).decode().strip()
    return decrypted_text

# Main program
if __name__ == "__main__":
    # Generate a 16-byte key
    key = input("Enter a 16-character key for encryption: ").encode()

    if len(key) != 16:
        print("Error: The key must be exactly 16 characters.")
        exit()

    # User input for plaintext
    plaintext = input("Enter the text you want to encrypt: ")
    padded_text = pad(plaintext)

    # Encrypt the plaintext
    nonce, ciphertext = encrypt_text(key, padded_text)
    print(f"Encrypted text: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt_text(key, nonce, ciphertext)
    print(f"Decrypted text: {decrypted_text}")
