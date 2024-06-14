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

from utils import hex_to_bytearray
from utils import scorePlaintext
from utils import single_byte_xor

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














# from collections import Counter
# Function that takes key and byte array as input --> returns XOR result
# def single_byte_xor(bytes_result: bytes, key: int) -> bytes:
#     """
#     Given a plain text `text` as bytes and an encryption key `key` as a byte
#     in range [0, 256) the function encrypts the text by performing
#     XOR of all the bytes and the `key` and returns the resultant.
#     """
#     return bytes([b ^ key for b in bytes_result])

# # Compute the fitting quotient for the decoded bytes
# def compute_fitting_quotient(bytes_result):
#     """
#     Given the stream of bytes `text` the function computes the fitting
#     quotient of the letter frequency distribution for `text` with the
#     letter frequency distribution of the English language.

#     The function returns the average of the absolute difference between the
#     frequencies (in percentage) of letters in `text` and the corresponding
#     letter in the English Language.
#     """
#     counter = Counter(bytes_result)
#     dist_text = [
#         (counter.get(ord(ch), 0) * 100 / len(bytes_result))
#         for ch in occurance_english
#     ]
#     return sum([abs(a - b) for a, b in zip(dist_english, dist_text)]) / len(dist_english)

# def decipher(bytes_result):
#     """
#     The function deciphers an encrypted text using Single Byte XOR and returns
#     the original plain text message and the encryption key.
#     """
#     original_text, encryption_key, min_fq = None, None, float('inf')
#     # generate the plain text using the encryption key 'k'
#     for k in range(256):
#         _text = single_byte_xor(bytes_result, k)
    
#     # compute the fitting quotient for this decrypted plain text
#         _fq = compute_fitting_quotient(_text)

#         # if the fitting quotient of this generated plain text is lesser
#         # than the minimum seen til now, update 'min_fq'
#         if min_fq is None or _fq < min_fq:
#             encryption_key, original_text, min_fq = k, _text, _fq
    
#     # Return the text and key that has the minimum fitting quotient
#     return original_text, encryption_key

# # Decode hex into binary (byte array)
# hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
# bytes_result = bytes.fromhex(hex_string)

# occurance_english = {
#     'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
#     'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
#     'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
#     'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
#     'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
#     'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
#     'y': 1.9913847,    'z': 0.0746517
# }

# # Distribution of letters in English
# dist_english = list(occurance_english.values())

# result, key = decipher(bytes_result)
# decoded_message = single_byte_xor(result, key)
# print(f"Decoded bytes: {bytes_result}")
# print(f"Decoded message: {decoded_message.decode('ascii', errors="ignore")}")
# print(f"Key: {key}")
