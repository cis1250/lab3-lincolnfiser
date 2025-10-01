# Fibonacci Sequence Exercise

while True:
    try:
        terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
        if terms > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a positive integer.")

# Calculate Fibonacci sequence
a, b = 0, 1
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b

print()  # newline at the end
