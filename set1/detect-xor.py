"""
Cryptopals Challenge Set 1 Challenge 4

Detect single-character XOR
One of the 60 character strings in this file has been encrypted by
single-character XOR. 

Find it. 

(Your code from #3 should help.)
"""
import sys
import os

# Add parent directory to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import hex_to_bytearray
from utils.utils import single_byte_xor
from utils.utils import scorePlaintext

decoded_strings = []

with open("4.txt") as file:
    for line in file:
        line = line.strip()
        byteArray = hex_to_bytearray(line)
        decoded_strings.append(byteArray)

bestScore = 0
bestKey = None
bestPlaintext = ""

for string in decoded_strings:
    for key in range(256):
        potential_plaintext = single_byte_xor(string, key)
        try:
            decoded_text = potential_plaintext.decode('utf-8')
        except UnicodeDecodeError:
            continue

        score = scorePlaintext(decoded_text)

        if score > bestScore:
            bestScore = score
            bestKey = key
            bestPlaintext = decoded_text

print(f"Best Key: {bestKey}")
print(f"Message: {bestPlaintext}")