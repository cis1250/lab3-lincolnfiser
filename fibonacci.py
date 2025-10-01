# Simple Fibonacci sequence

# Ask user for number of terms
terms = input("Enter the number of terms: ")

# Keep asking until a positive integer is entered
while not terms.isdigit() or int(terms) <= 0:
    print("Please enter a positive integer.")
    terms = input("Enter the number of terms: ")

terms = int(terms)

# Generate Fibonacci sequence
a = 0
b = 1
for i in range(terms):
    print(a)
    temp = a + b
    a = b
    b = temp
