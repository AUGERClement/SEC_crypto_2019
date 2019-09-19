#!/bin/python3

from os import sys
import base64

def reader(filename):
    try:
        with open(filename) as file:
            content = file.read().rstrip()
    except:
        quit(84)
    return content

if (len(sys.argv) < 0):
    quit(84)

content = reader(sys.argv[1])

if (len(content) == 0):
    quit(84)


hexa = bytes.fromhex(content)
sixtyfour = base64.b64encode(hexa)

print(sixtyfour.decode())