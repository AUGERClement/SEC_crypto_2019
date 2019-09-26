##
# Challenge08
# 
# Usage: ./challenge08 fileName
# 
# fileName must contain a bunch of base64-encoded strings.
# One of them is an ECB-encrypted cyphertext.
# 
# This program detects it and outputs the line number.
##

#!/bin/python3

import sys
import base64

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def reader(fileName):
    try:
        with open(fileName) as f:
            content = f.read().rstrip().split('\n')         # rstrip ne sert a rien ?
    except Exception as e:
        eprint(e)
        quit(84)
    return content

# Program's core
def compareBlocks(line):
    for a, b in zip(line, line[1:]):
        if a == b:
            return True
    return False

def isEncrypted(line):
    message = base64.decodebytes(line.encode())
    return compareBlocks([ message[x:x+16] for x in range(0, len(message), 16) ])

def AESDetect(fileInput):
    for i, line in enumerate(fileInput):
        if isEncrypted(line):
            return i + 1

    # ECB-encrypted cyphertext found
    eprint("Corrupted file: no correspondance found.")
    quit(84)


# Parsing and call of functions
if __name__ == '__main__':
    if len(sys.argv) < 2:
        eprint("Bad number of argument: You have to give at least 2 arguments.")
        quit(84)
    
    # Now that we know we've got a file name, let's read it
    fileInput = reader(sys.argv[1])
    print(AESDetect(fileInput))