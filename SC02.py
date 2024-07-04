import binascii

def fixed_xor(hex1, hex2):
    # Convert hex strings to bytes
    bytes1 = binascii.unhexlify(hex1)
    bytes2 = binascii.unhexlify(hex2)
    
    # XOR the bytes
    xor_bytes = bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
    
    # Convert bytes back to hex
    return binascii.hexlify(xor_bytes).decode()

# Example usage
hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"
result = fixed_xor(hex_string1, hex_string2)
print(result)
