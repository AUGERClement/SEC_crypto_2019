#!/bin/python3

from os import sys

def reader(filename):
    try:
        with open(filename) as file:
            content = file.read().rstrip()
        hex_content = bytes.fromhex(content)
    except:
        quit(84)

    if (len(content) == 0):
        quit(84)
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
            hamming_dists.append((get_hamming_distance(piece1, piece2) / keysize))
            i += 2
        result = {
            'keysize':keysize,
            'avg distance': (sum(hamming_dists) / len(hamming_dists))
        }
        average_distances.append(result)
    #sort list and take the couple of lower avg dist
    key = sorted(average_distances, key=lambda x: x['avg distance'])[0]
    key2 = sorted(average_distances, key=lambda x: x['avg distance'])[1]
    #print(key['avg distance'])
    #print(key['keysize'])
    return key['keysize'], key2['keysize']




if __name__ == "__main__":
    if (len(sys.argv) != 2):
        quit(84)
    
    #get content hex from file
    content = reader(sys.argv[1])
    key_length, key2_length = get_keysize(content)

    key = []
    key2 = []
    true_key = []

    #break cipher into block with each nth char inside
    #problable problem in those lines.
    for i in range(key_length):
        block = b''
        for j in range (i, len(content), key_length):
            block += bytes([content[j]])
        key.append(bruteforce(block))

    for i in range(key2_length):
        block = b''
        for j in range (i, len(content), key2_length):
            block += bytes([content[j]])
        key2.append(bruteforce(block))




    #for byte in key:
    #    print('{:02X}'.format(byte), end='')
    #print()

    for byte in key2:
        print('{:02X}'.format(byte), end='')
    print()