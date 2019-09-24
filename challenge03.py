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


def bruteforce_single_key(content):
    hexa = bytes.fromhex(content)
    result = b''
    key, score = 0, 0
    scoretmp = 0

    for bruteforcekey in range(256):
        result = char_xor(hexa, bruteforcekey)

        scoretmp = get_score(result)
        if (scoretmp > score):
            key, score = bruteforcekey, scoretmp 
    return key


if __name__ == "__main__":
    #get content hex from file
    content = reader(sys.argv[1])
    key = bruteforce_single_key(content)
    print('{:02X}'.format(key))