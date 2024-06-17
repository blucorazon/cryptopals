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
import sys
import os

# Add parent directory to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import hamming_distance

# TODO: Read the encrypted data from the file


# TODO: Compute the Hamming distance between two strings
str1 = 'this is a test'
str2 = 'wokka wokka!!!'

print(f"Hamming distance: {hamming_distance(str1, str2)}")

KEYSIZE = list(range(2, 41))