# Fibonacci Sequence Exercise

while True:
    user_input = input("Enter the number of terms in the Fibonacci sequence: ")

    # Validate input
    if user_input.isdigit() and int(user_input) > 0:
        terms = int(user_input)
        break
    else:
        print("Please enter a positive integer.")

# Calculate Fibonacci sequence
fib_sequence = []
a, b = 0, 1
for _ in range(terms):
    fib_sequence.append(a)
    a, b = b, a + b

# Print all numbers in one line
print(" ".join(map(str, fib_sequence)))





#!/usr/bin/env python3
# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

