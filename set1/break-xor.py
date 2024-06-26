"""
Cryptopals Challenge Set 1 Challenge 6
There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

2. Write a function to compute the edit distance/Hamming distance between two 
strings. The Hamming distance is just the number of differing bits. The 
distance between:

this is a test

and

wokka wokka!!!

is 37. Make sure your code agrees before you proceed.

3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, 
and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

4. The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed 
perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.

5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

6. Now transpose the blocks: make a block that is the first byte of every block, 
and a block that is the second byte of every block, and so on.

7. Solve each block as if it was single-character XOR. You already have code to do this.

8. For each block, the single-byte XOR key that produces the best looking histogram is 
the repeating-key XOR key byte for that block. Put them together and you have the key.
"""
import base64
from utils.utils import find_key_length

with open("6.txt", "r") as file:
    # Read the base64-encoded data from the file
    base64_data = file.read()

# Decode base64 to binary and store in byte array
byte_array = bytearray(base64.b64decode(base64_data))

# Determine the most likely Keysize candidate
KEYSIZE = find_key_length(byte_array)

print(f"The keysize with the smallest normalized edit distance is: {KEYSIZE}")

# Break the ciphertext into blocks of KEYSIZE length
for i in range(0, len(byte_array)):
    block = byte_array[i * KEYSIZE : (i + 1) * KEYSIZE]

transposed_blocks = [[] for _ in range(KEYSIZE)]

# TODO: Transpose the blocks
for byte in block:
    transposed_blocks.append(byte)

# TODO: Solve each block as if it was single byte XOR

# TODO: For each block the highest scoring XOR key is the repeating-key xor key byte for that block
# Append them as you iterate through the block to create the key