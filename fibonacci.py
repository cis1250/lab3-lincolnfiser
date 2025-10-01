#!/usr/bin/env python3

# Fibonacci Sequence Exercise

# Step 1: Prompt the user
while True:
    user_input = input("Enter the number of terms: ")
    
    # Step 2: Validate input
    if int(user_input) > 0:
        terms = int(user_input)
        break
    else:
        print("Please enter a positive integer.")

# Step 3: Calculate and print Fibonacci sequence
a, b = 0, 1
for i in range(terms):
    print(a)
    a, b = b, a + b

print()  # print a new line at the end
