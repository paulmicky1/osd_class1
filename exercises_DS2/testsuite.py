'''
	python0.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''

import unittest
from prime import is_prime  # Import the function from prime.py

class TestPrime(unittest.TestCase):
    def test_small_prime_numbers(self):
        """Test small known prime numbers"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_small_non_prime_numbers(self):
        """Test small known non-prime numbers"""
        self.assertFalse(is_prime(1))  # Edge case: 1 is not prime
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

    def test_large_prime_numbers(self):
        """Test large prime numbers"""
        self.assertTrue(is_prime(9007199254740991))  # Known large prime number
        self.assertTrue(is_prime(9007195909437503))  # Another known prime

    def test_large_non_prime_numbers(self):
        """Test large composite numbers"""
        self.assertFalse(is_prime(9007199254740992))  # One more than a prime
        self.assertFalse(is_prime(1000000000000000))  # Clearly composite

if __name__ == "__main__":
    unittest.main()
