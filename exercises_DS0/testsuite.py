
'''
	python0.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''

import unittest
from fizzbuzz import fizzbuzz  # Import the function from fizzbuzz.py

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        """Test if numbers divisible by 3 return 'Fizz'"""
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")

    def test_buzz(self):
        """Test if numbers divisible by 5 return 'Buzz'"""
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_fizzbuzz(self):
        """Test if numbers divisible by both 3 and 5 return 'FizzBuzz'"""
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_number(self):
        """Test if other numbers return themselves as strings"""
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(7), "7")

if __name__ == "__main__":
    unittest.main()
