import binascii
import base64

def hex_to_base64(hex_string):
    # Convert hex to bytes
    byte_data = binascii.unhexlify(hex_string)
    # Convert bytes to base64
    base64_data = base64.b64encode(byte_data)
    return base64_data

# Example usage:
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
result = hex_to_base64(hex_string)
print(result)
