'''
	python0.py

	Copyright (c) PAUL MICKY D COSTA
	Licensed under the MIT license: https://opensource.org/license/mit
'''


import math

class Rational:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        # Simplify the fraction by dividing by GCD
        gcd_value = Rational.gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd_value
        self.denominator //= gcd_value

        # Ensure the denominator is always positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def negate(self):
        # Negates the fraction (change the sign of numerator)
        self.numerator = -self.numerator

    def invert(self):
        # Swaps numerator and denominator (fraction inversion)
        self.numerator, self.denominator = self.denominator, self.numerator
        self.reduce()

    def cmp(self, other):
        # Compare the fraction with another Rational object
        val1 = self.numerator * other.denominator
        val2 = self.denominator * other.numerator

        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1
        else:
            return 0

    def to_string(self):
        # Return a string representation of the fraction
        if self.numerator == 0:
            return "0"
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def add(self, other):
        # Add two fractions
        num = self.numerator * other.denominator + self.denominator * other.numerator
        denom = self.denominator * other.denominator
        return Rational(num, denom)

    def sub(self, other):
        # Subtract two fractions
        num = self.numerator * other.denominator - self.denominator * other.numerator
        denom = self.denominator * other.denominator
        return Rational(num, denom)

    def mul(self, other):
        # Multiply two fractions
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return Rational(num, denom)

    def div(self, other):
        # Divide two fractions (raises error for division by zero)
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        num = self.numerator * other.denominator
        denom = self.denominator * other.numerator
        return Rational(num, denom)


# Function to take user input for creating a Rational object
def get_rational_input(prompt="Enter a rational number (numerator/denominator or just numerator): "):
    try:
        # Get input from the user
        user_input = input(prompt)

        # Check if the input is of the form 'numerator/denominator'
        if '/' in user_input:
            numerator, denominator = map(int, user_input.split('/'))
            return Rational(numerator, denominator)
        else:
            # If only numerator is given, default denominator to 1
            return Rational(int(user_input), 1)
    except ValueError:
        print("Invalid input. Please enter integers.")
        return get_rational_input(prompt)


def main():
    print("Welcome to the Rational Numbers Calculator!")

    # Input two rational numbers from the user
    print("\nEnter the first rational number:")
    r1 = get_rational_input()

    print("\nEnter the second rational number:")
    r2 = get_rational_input()

    # Display the entered rational numbers
    print("\nFirst Rational Number: ", r1.to_string())
    print("Second Rational Number: ", r2.to_string())

    # Perform some operations
    print("\nPerforming operations on the two fractions...\n")

    # Addition
    add_result = r1.add(r2)
    print(f"Addition: {r1.to_string()} + {r2.to_string()} = {add_result.to_string()}")

    # Subtraction
    sub_result = r1.sub(r2)
    print(f"Subtraction: {r1.to_string()} - {r2.to_string()} = {sub_result.to_string()}")

    # Multiplication
    mul_result = r1.mul(r2)
    print(f"Multiplication: {r1.to_string()} * {r2.to_string()} = {mul_result.to_string()}")

    # Division
    try:
        div_result = r1.div(r2)
        print(f"Division: {r1.to_string()} / {r2.to_string()} = {div_result.to_string()}")
    except ValueError:
        print(f"Error: Cannot divide {r1.to_string()} by {r2.to_string()} (division by zero)")

    # Comparison
    comparison_result = r1.cmp(r2)
    if comparison_result == 0:
        print(f"Comparison: {r1.to_string()} is equal to {r2.to_string()}")
    elif comparison_result == 1:
        print(f"Comparison: {r1.to_string()} is greater than {r2.to_string()}")
    else:
        print(f"Comparison: {r1.to_string()} is smaller than {r2.to_string()}")

    # Negation and Inversion
    r1.negate()
    print(f"Negated first rational number: {r1.to_string()}")

    r2.invert()
    print(f"Inverted second rational number: {r2.to_string()}")


if __name__ == "__main__":
    main()
