""" 
Cryptopals Set 1, Challenge 1: Convert hex to base64

The string:
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

Should produce:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

Cryptopals Rule:
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
"""
import base64
import binascii

# Decode hex with binascii module
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bytes_result = binascii.unhexlify(hex_string)

print(f"Hex String: {hex_string}")
print(f"Decoded Message: {bytes_result}")

# Encode bytes using Base64
base64_bytes = base64.b64encode(bytes_result)

print(f"Base64: {base64_bytes}")