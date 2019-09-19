#!/bin/python3

from os import sys

def reader(filename):
    try:
        with open(filename) as file:
            content = file.read().rstrip()
    except:
        quit(84)
    return content


if (len(sys.argv) != 2):
    quit(84)

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

#get content hex from file
content = bytes.fromhex(reader(sys.argv[1]))

 #bytes arr
result = b''
key, score = 0, 0
scoretmp = 0

for bruteforcekey in range(256):
    result = char_xor(content, bruteforcekey)

    scoretmp = get_score(result)
    if (scoretmp > score):
        key, score = bruteforcekey, scoretmp 


print('{:02X}'.format(key))