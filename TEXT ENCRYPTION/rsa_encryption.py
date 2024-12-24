from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA keys
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Encrypt using RSA
def rsa_encrypt(public_key, plaintext):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext).decode()

# Decrypt using RSA
def rsa_decrypt(private_key, ciphertext):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_text = cipher.decrypt(base64.b64decode(ciphertext)).decode()
    return decrypted_text

# Main program
if __name__ == "__main__":
    print("=== RSA Encryption Program ===")

    # Generate RSA key pair
    private_key, public_key = generate_rsa_keys()

    print("\n=== Generated Keys ===")
    print(f"Public Key:\n{public_key.decode()}")
    print(f"Private Key:\n{private_key.decode()}")

    # Get user input
    plaintext = input("\nEnter the text to encrypt: ")

    # Perform encryption
    encrypted_text = rsa_encrypt(public_key, plaintext)
    print(f"\nEncrypted text: {encrypted_text}")

    # Perform decryption
    decrypted_text = rsa_decrypt(private_key, encrypted_text)
    print(f"Decrypted text: {decrypted_text}")
