#!/usr/bin/env python3

# Fibonacci Sequence Exercise

while True:
    user_input = input("Enter the number of terms in the Fibonacci sequence: ")

    # Validate input
    if user_input.isdigit() and int(user_input) > 0:
        terms = int(user_input)
        break
    else:
        print("Please enter a positive integer.")

# Calculate and print Fibonacci sequence
a, b = 0, 1
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b

print()  # new line at the end



#!/usr/bin/env python3
# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

