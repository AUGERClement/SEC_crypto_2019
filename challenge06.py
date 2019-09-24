#!/bin/python3

from os import sys

def reader(filename):
    try:
        with open(filename) as file:
            content = file.read().rstrip()
    except:
        quit(84)

    hex_content = bytes.fromhex(content)
    return hex_content

#get hamming dist between two bytes arr (step1)
def get_hamming_distance(bytes1, bytes2):
    i = 0

    #zip stop when the shorter list is reached
    for byte1, byte2 in zip(bytes1, bytes2):
        xored = byte1 ^ byte2

        #sum of a list of xored bytes (differents bytes)
        i += sum([1 for bit in bin(xored) if bit == '1'])

    return i


#xor the string with the single byte key
def char_xor(content, key):
    result = b'' #array of bytes to stock res


    for byte in content:
        result += bytes([byte ^ key])
    
    return result

def get_score(result):
    """to define a eng score, we will count the number of
    occurences of commons eng char. The more it has, the most it may be eng"""

    cpt = 0
    needles = b"etaioin shrdlu"

    for byte in result:
        if byte in needles:
            cpt += 1
    return cpt

#bruteforce a line (hex bytes arr). Step 2
def bruteforce(line):

    result = b''
    key, score = 0, 0
    scoretmp = 0

    for bruteforcekey in range(256):
        result = char_xor(line, bruteforcekey)

        scoretmp = get_score(result)
        if (scoretmp > score):
            key, score = bruteforcekey, scoretmp
    print('{:02X}'.format(key), end='')
    return key


#try to get differents keysize. Valid fonction
def get_keysize(content):
    average_distances = []
    for keysize in range (2, 42):
        i = 0
        hamming_dists = []

        #split every KEYSIZE th elem. Use list comprehension
        pieces = [content[i:i + keysize] for i in range(0, len(content), keysize)]

        while i < len(pieces) - 1:
            piece1 = pieces[i]
            piece2 = pieces[i + 1]

            #get hamming distance between two parts of the message
            hamming_dists.append(get_hamming_distance(piece1, piece2) / keysize)
            i += 2
        result = {
            'keysize':keysize,
            'avg distance': sum(hamming_dists) / len(hamming_dists)
        }
        average_distances.append(result)
    #sort list and take the lower avg dist, with his keysize
    key_length = sorted(average_distances, key=lambda x: x['avg distance'])[0]['keysize']
    return key_length




if __name__ == "__main__":
    if (len(sys.argv) != 2):
        quit(84)
    
    #get content hex from file
    content = reader(sys.argv[1])
    key_length = get_keysize(content)

    key = b''

    #print(key_length) #Correct key_length

    #break cipher into block with each nth char inside
    #problable problem in those lines.
    for i in range(key_length):
        block = b''
        for j in range (i, len(content), key_length):
            block += bytes([content[j]])
        key += bytes(bruteforce(block))

    print()