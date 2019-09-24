#!/bin/python3

from os import sys
import base64

def reader(filename):
    try:
        with open(filename) as file:
            content = file.read().rstrip().split('\n')
    except:
        quit(84)
    return content

def bxor(b1, b2):
    result = b""
    for b1, b2 in zip(b1, b2):
        result += bytes([b1 ^ b2])
    return result

#xor two string of char. Convert them to hex, call bxor to xor them, and then reconvert to hex.
def xor_str(str1, str2):
    bytes1 = bytes.fromhex(str1)
    bytes2 = bytes.fromhex(str2)

    if (len(bytes1) != len(bytes2)):
        quit(84)
    bytes3 = bxor(bytes1, bytes2)

    solution = bytes3.hex()

    return solution.upper()




if __name__ == "__main__":
    if (len(sys.argv) < 0):
        quit(84)

    content = reader(sys.argv[1])

    if (len(content) != 2):
        quit(84)


    xored = xor_str(content[0], content[1])
    print(xored)