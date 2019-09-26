##
# Challenge 04
# 
# Create a file containing one hex-encoded string per line, among 
# wich one has been encrypted by a single-byte XOR, write a program
# that detects this string, decrypts it (in the 3rd challenge fashion)
# and prints the key used to encrypt it in hexadecimal, prefixed with
# the line number.
# 
##
# !/bin/python3

import unittest
from challenge04 import reader, detector

class TestChallenge04(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(reader("testFile/input01.txt"), [bytes.fromhex(n) for n in ["4B"]])

    def test_not_existing_file(self):
        with self.assertRaises(SystemExit) as ret:
            reader("not_existing_file")
        self.assertEqual(ret.exception.code, 84)
