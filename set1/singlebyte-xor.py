"""
Cryptopals Challenge Set 1, Challenge 3

Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency 
is a good metric. Evaluate each output and choose the one with the best score.
"""
import sys
import os

# Add parent directory to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import hex_to_bytearray
from utils.utils import scorePlaintext
from utils.utils import single_byte_xor

# Decode hex string into byte array
hexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
byteArray = hex_to_bytearray(hexString)

bestScore = 0
bestKey = None
bestPlaintext = ""

# For each key, perform an XOR operation between byte array and key
for key in range(256):
    potential_plaintext = single_byte_xor(byteArray, key)
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