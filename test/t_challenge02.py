##
# Challenge 02
# 
# Write a program that takes a file containing two hexadecimal
# encoded buffers if equal (and only equal) length separated 
# by a newline and produces their XOR combination.
# 
##
# !/bin/python3

import unittest
from challenge02 import reader, xor_str

class TestChallenge02(unittest.TestCase):
    
    def test_read_file(self):
        self.assertEqual(reader("testFile/input01.txt"), ["4B"])

    def test_not_existing_file(self):
        with self.assertRaises(SystemExit) as ret:
            reader("not_existing_file")
        self.assertEqual(ret.exception.code, 84)

    def test_xor_little_number(self):
        self.assertEqual(xor_str("5374616C6C6D616E", "426C61636B486174"), "1118000F0725001A")

    def test_non_equal_length_number(self):
        with self.assertRaises(SystemExit) as ret:
            xor_str("125789", "123456789")
        self.assertEqual(ret.exception.code, 84)