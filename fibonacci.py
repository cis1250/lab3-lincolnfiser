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


