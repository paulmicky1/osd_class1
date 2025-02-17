'''
	python0.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''
import unittest
from prime_checker import is_prime

class TestPrimeChecker(unittest.TestCase):

    def test_small_prime(self):
        self.assertEqual(is_prime(5), "true")  # 5 is prime
    
    def test_small_composite(self):
        self.assertEqual(is_prime(4), "false")  # 4 is composite
    
    def test_large_composite_1(self):
        self.assertEqual(is_prime(9007199254740991), "false")  # 9007199254740991 is not prime
    
    def test_large_composite_2(self):
        self.assertEqual(is_prime(9007195909437503), "false")  # 9007195909437503 is not prime
    
    def test_small_number(self):
        self.assertEqual(is_prime(1), "false")  # 1 is not prime
    
    def test_edge_case(self):
        self.assertEqual(is_prime(0), "false")  # 0 is not prime
    
    def test_prime_2_and_3(self):
        self.assertEqual(is_prime(2), "true")  # 2 is prime
        self.assertEqual(is_prime(3), "true")  # 3 is prime

if __name__ == '__main__':
    unittest.main()
