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

import unittest
from challenge04 import reader, detector

class TestChallenge04(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(reader("testFile/input01.txt"), [bytes.fromhex(n) for n in ["4B"]])

    def test_not_existing_file(self):
        with self.assertRaises(SystemExit) as ret:
            reader("not_existing_file")
        self.assertEqual(ret.exception.code, 84)

    def test_index(self):
        index, _ = detector("BD969CE5A2B882F59391A59EF9FBEE94E7BA8C92E587B3F6E389E08B89B6B694BC809CFDE5F210110D70125E48035E1C0355734C6B7C75096646475E1754085C4E156B7540446F706D78531ADFCEC0CF8096C282D5F6F1CDDB9B89FDC1FFD2C5EA8988D48FD2E09FF9CA96F891C9D696D9D96D76662F487334375F5B402F584A3F6C217D535A27214941256A3257736E36463A6E5163723E9D86EADDC8E3EED9ED88C5CCFADC9E92C4C0C381DDF785C6FCC2E1F88290D28FE3D8ECC7DC9")
        self.assertEqual(index, 440)