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

if (len(sys.argv) < 2):
    quit(84)

if (len(content) == 0):
    quit(84)


#convert a HEX str to base 64.
def hex_convertisser(content):

    hexa = bytes.fromhex(content)
    sixtyfour = base64.b64encode(hexa)

    return sixtyfour.decode()



#main event
content = reader(sys.argv[1])
converted = hex_convertisser(content)

print (converted)