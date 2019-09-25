#!/bin/python3

from os import sys

def reader(filename):
    try:
        with open(filename) as file:
            content = file.read().rstrip().split('\n')
    except:
        quit(84)

    if (len(content) == 2):
        quit(84)
    try:
        content = [bytes.fromhex(line) for line in content]
    except:
        quit(84)
    return content[0], content[1]


if (len(sys.argv) != 2):
    quit(84)

#xor the string with the key (array of bytes)
def encode_xor(content, key):
    result = b'' #array of bytes to stock res
    i = 0 #iterator on key
    length = len(key)


    for byte in content:
        result += bytes([byte ^ key[i]])
        i += 1
        if (i == length):
            i = 0
    
    return result.hex().upper()


if __name__ == "__main__":
    #get content hex from file
    key, content = reader(sys.argv[1])
    result = encode_xor(content, key)

    print(result)