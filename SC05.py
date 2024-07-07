def repeating_key_xor(plaintext, key):
    # Convert plaintext and key to bytes
    plaintext_bytes = plaintext.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    # Initialize the result as an empty bytearray
    result = bytearray()
    
    # Perform repeating-key XOR
    for i in range(len(plaintext_bytes)):
        result.append(plaintext_bytes[i] ^ key_bytes[i % len(key_bytes)])
    
    # Convert the result to hexadecimal
    hex_result = result.hex()
    return hex_result

# Given plaintext and key
plaintext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"

# Encrypt the plaintext using the repeating-key XOR function
encrypted_text = repeating_key_xor(plaintext, key)
print(encrypted_text)
