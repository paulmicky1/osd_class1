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
        self.assertTrue(is_palindrome("Renener"))  # Added test case

    def test_non_palindromes(self):
        """Test words that are not palindromes"""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_case_insensitivity(self):
        """Test case insensitivity"""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("MadAm"))
        self.assertTrue(is_palindrome("Renener"))  # Case insensitive check

if __name__ == "__main__":
    unittest.main()