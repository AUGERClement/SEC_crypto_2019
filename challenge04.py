#!/bin/python3

from os import sys

def reader(filename):
    try:
        with open(filename) as file:
            content = file.read().rstrip().split('\n')
    except:
        quit(84)

    content = [bytes.fromhex(line) for line in content]
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

#bruteforce a line (hex bytes arr)
def bruteforce(line):

    result = b''
    key, score = 0, 0
    scoretmp = 0

    for bruteforcekey in range(256):
        result = char_xor(line, bruteforcekey)

        scoretmp = get_score(result)
        if (scoretmp > score):
            key, score = bruteforcekey, scoretmp 
    return key, score

#detect a single byte xor in a list of str (hex converted)
def detector(content):
    index, indextmp = 0, 0 #index of the line, and his tmp
    key, score = 0, 0 #key and score of the closest english-like text
    keytmp, scoretmp = 0, 0 #key and score for the tested lines

    for line in content:
        keytmp, scoretmp = bruteforce(line)
        if (scoretmp > score):
            key, score, index = keytmp, scoretmp, indextmp
        indextmp += 1
    return index, key


if __name__ == "__main__":
    #get content hex from file
    content = reader(sys.argv[1])

    index, key = detector(content)
    #index may need a incrementation depending of the moulinette
    print(index, '{:02X}'.format(key))