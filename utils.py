"""
Helpful Functions Through the Cryptopals Challenges
"""

"""Functions that decode a hex string into bytes """
import binascii
# Decode hex with bytes.fromhex() function
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bytes_result = bytes.fromhex(hex_string)

print(type(hex_string))
print(bytes_result)
print(type(bytes_result))

# Decode hex with bytearray.fromhex() function
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bytearray_result = bytearray.fromhex(hex_string)

print(type(hex_string))
print(bytearray_result)
print(type(bytearray_result))

# Decode hex with binascii module and unhexlify() function
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
bytes_result = binascii.unhexlify(hex_string)

print(type(hex_string))
print(bytes_result)
print(type(bytes_result))