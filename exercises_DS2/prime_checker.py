'''
	python0.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''
import math

def is_prime(n):
    if n <= 1:
        return "false"
    if n == 2:
        return "true"  # 2 is prime
    if n % 2 == 0:
        return "false"  # Exclude even numbers greater than 2
    
    # Check divisibility from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return "false"
    return "true"

# Code to check if the script is run directly
if __name__ == '__main__':
    # Prompt the user for a number
    number = int(input("Enter a number to check if it's prime: "))
    # Call the is_prime function and print the result
    print(f"The number {number} is prime: {is_prime(number)}")
