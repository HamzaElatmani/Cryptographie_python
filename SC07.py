from Crypto.Cipher import AES
import base64

# Read the encrypted content from the file
file_path = "/mnt/data/image.png"  # Replace with the actual path to your file
with open(file_path, 'rb') as file:
    encrypted_base64 = file.read()

# Decode the Base64-encoded content
encrypted_data = base64.b64decode(encrypted_base64)

# Define the key (16 bytes for AES-128)
key = b"YELLOW SUBMARINE"

# Create the AES cipher in ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Decrypt the content
decrypted_data = cipher.decrypt(encrypted_data)

# Convert the decrypted bytes to a string (assuming it is text)
decrypted_text = decrypted_data.decode('utf-8')

print(decrypted_text)
