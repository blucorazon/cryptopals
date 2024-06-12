"""
Cryptopals Challenge Set 1, Challenge 2

Fixed XOR
Write a function that takes two equal-length buffers and produces
their XOR combination. If your function works properly, then when 
you feed it the string:

"1c0111001f010100061a024b53535009181c"

...after hex decoding, and when XOR'd against"
"686974207468652062756c6c277320657965"

...should produce:
746865206b696420646f6e277420706c6179
"""
# Function to produce the XOR combination of two equal length buffers
def fixed_xor(hex_string1, hex_string2):
    
    # Decode hex to binary
    bytes1 = bytearray.fromhex(hex_string1)
    bytes2 = bytearray.fromhex(hex_string2)
    
    # Perform bitwise operation on both variables
    xor_result = bytes(a ^ b for a, b in zip(bytes1, bytes2))
    
    # Convert binary back to hex format
    hex_result = xor_result.hex()
    
    return hex_result

hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

result = fixed_xor(hex_string1, hex_string2)

print(f"Hex String 1: {hex_string1}")
print(f"Hex String 2: {hex_string2}")
print(f"Fixed XOR result: {result}")
