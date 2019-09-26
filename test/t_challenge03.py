##
# Challenge 03
# 
# Code a program that finds the single byte key that has 
# been XORed againt a given string.
# The input is a hexadecimal encoded file.
# The byte used for the XOR operation should be printed 
# on the standard output in capital hexadecimal.
# 
##
# !/bin/python3

import unittest
from challenge03 import reader, bruteforce_single_key

class TestChallenge03(unittest.TestCase):

    def test_read_file(self):
        self.assertEqual(reader("testFile/input01.txt"), "4B")

    def test_not_existing_file(self):
        with self.assertRaises(SystemExit) as ret:
            reader("not_existing_file")
        self.assertEqual(ret.exception.code, 84)

    def test_xor_cipher(self):
        self.assertEqual('{:02X}'.format(bruteforce_single_key("0430272762112D243635233027786204302727262D2F62232C2662012D2D32273023362B2D2C")), "42")
