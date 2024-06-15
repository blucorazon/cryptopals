"""
Cryptopals Challenge Set 1 Challenge 5

Implement repeating-key XOR
Here is the opening stanza of an important work of the English language:

Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the 
first byte of plaintext will be XOR'd against I, the next C, the next E, 
then I again for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
"""
import binascii
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import repeating_key_xor

def format_with_line_breaks(hex_str, line_length=60):
    return '\n'.join([hex_str[i:i+line_length] for i in range(0, len(hex_str), line_length)])

# Read from file
with open("dickens.txt") as file:
    # Convert the string to bytes
    byteArray = bytearray(file.read(), 'utf-8')
key = bytes('ICE', 'utf-8')

encrypted = repeating_key_xor(byteArray, key)

hex_encrypted = binascii.hexlify(encrypted).decode('utf-8')
formatted_text = format_with_line_breaks(hex_encrypted)

with open('output.txt', 'w') as output_file:
    output_file.write(formatted_text)