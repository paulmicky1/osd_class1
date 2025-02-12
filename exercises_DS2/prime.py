'''
	python0.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''


import math

def is_prime(n):
    """Returns True if the given number is prime, False otherwise."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisibility using 6k ± 1 rule for efficiency
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a positive integer to check for primality (or 0 to exit): "))
            if num == 0:
                break
            print(f"Prime: {is_prime(num)}")
        except ValueError:
            print("Please enter a valid positive integer.")
