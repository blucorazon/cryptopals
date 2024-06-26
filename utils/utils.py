"""
Helpful Functions Through the Cryptopals Challenges
"""
# Decode hex with bytes.fromhex() function
def hex_to_bytes(string):
    return  bytes.fromhex(string)

# Decode hex with bytearray.fromhex() function
def hex_to_bytearray(string):
    return bytearray.fromhex(string)

def single_byte_xor(byte_array, key):
    return bytes([a ^ key for a in byte_array])

def test_single_byte_xor():
    plaintext = "hello"
    key = 42
    byte_array = bytearray(plaintext, 'utf-8')

    # Encrypt the plaintext
    encrypted = single_byte_xor(byte_array, key)

    # Decrypt the encrypted message 
    decrypted = single_byte_xor(encrypted, key)

    if decrypted == byte_array: 
        print("Test Passed.")
    else:
        print("Test failed.")

def scorePlaintext(plaintext):
    letterFrequency = {
        'E' : 12.0,
        'T' : 9.10,
        'A' : 8.12,
        'O' : 7.68,
        'I' : 7.31,
        'N' : 6.95,
        'S' : 6.28,
        'R' : 6.02,
        'H' : 5.92,
        'D' : 4.32,
        'L' : 3.98,
        'U' : 2.88,
        'C' : 2.71,
        'M' : 2.61,
        'F' : 2.30,
        'Y' : 2.11,
        'W' : 2.09,
        'G' : 2.03,
        'P' : 1.82,
        'B' : 1.49,
        'V' : 1.11,
        'K' : 0.69,
        'X' : 0.17,
        'Q' : 0.11,
        'J' : 0.10,
        'Z' : 0.07,
        ' ' : 15.0
    }
    score = 0
    
    for character in plaintext:
        if character.upper() in letterFrequency:
            frequency = letterFrequency.get(character.upper(), 0)
            score += frequency
    return score

def repeating_key_xor(byte_array, key):
    i = 0
    arr = bytearray()
    for char in byte_array:
        xor = char ^ key[i]
        arr.append(xor)
        i += 1
        if i >= len(key):
            i = 0
    return arr

def hamming_distance(str1: bytes, str2: bytes) -> int:
    if len(str1) != len(str2):
        raise ValueError('The strings must be equal length')
    distance = 0
    for byte1, byte2 in zip(str1, str2):
        distance += bin(byte1 ^ byte2).count('1')
    return distance

def find_key_length(byte_array: bytes) -> int:
    smallest_distance = len(byte_array)
    best_keysize = None

    for keysize in range(2, 41):
        chunk1 = byte_array[0:keysize]
        chunk2 = byte_array[keysize:keysize*2]
        
        if len(chunk1) == len(chunk2):
            edit_distance = hamming_distance(chunk1, chunk2)
            normalized_distance = edit_distance / keysize

            if normalized_distance < smallest_distance:
                smallest_distance = normalized_distance
                best_keysize = keysize  
    return best_keysize