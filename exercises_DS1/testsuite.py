'''
	python0.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''

import unittest
from palindrome import is_palindrome  # Import the function from palindrome.py

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        """Test basic word palindromes"""
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    def test_non_palindromes(self):
        """Test words that are not palindromes"""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_phrase_palindromes(self):
        """Test palindromic phrases with spaces and punctuation"""
        self.assertTrue(is_palindrome("A man, a plan, a canal – Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_case_insensitivity(self):
        """Test case insensitivity"""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("MadAm"))

    def test_numbers_and_symbols(self):
        """Test numbers and symbols in palindromes"""
        self.assertTrue(is_palindrome("22/02/2022"))
        self.assertFalse(is_palindrome("12345"))

if __name__ == "__main__":
    unittest.main()
