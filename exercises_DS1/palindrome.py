'''
	python0.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''

import re

def is_palindrome(s):
    """Returns True if the given string is a palindrome, False otherwise."""
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if the string is equal to its reverse
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    while True:
        user_input = input("Enter a word or phrase to check (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print("Palindrome:", is_palindrome(user_input))
