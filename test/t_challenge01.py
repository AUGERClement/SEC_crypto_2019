##
# Challenge 01
# 
# Make a program that converts the content of the file given
# as the first argument from hexadecimal to base64 and prints
# it on the standart output.
# 
##
# !/bin/python3

import unittest
from challenge01 import reader, hex_convertisser

class TestChallenge01(unittest.TestCase):

    # Reader
    def test_read_file(self):
        self.assertEqual(reader("testFile/input01.txt"), "4B")

    def test_not_existing_file(self):
        with self.assertRaises(SystemExit) as ret:
            reader("not_existing_file")
        self.assertEqual(ret.exception.code, 84)

    # convert
    def test_hexa_to_deca_little_number(self):
        self.assertEqual(hex_convertisser("4B"), "Sw==")

    def test_hexa_to_deca_big_number(self):
        self.assertEqual(hex_convertisser("931A75331265"), "kxp1MxJl")
