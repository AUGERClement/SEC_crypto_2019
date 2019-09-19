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


if (len(sys.argv) < 0):
    quit(84)

content = reader(sys.argv[1])

if (len(content) != 2):
    quit(84)


bytes1 = bytes.fromhex(content[0])
bytes2 = bytes.fromhex(content[1])

bytes3 = bxor(bytes1, bytes2)

solution = bytes3.hex()

print(solution.upper())