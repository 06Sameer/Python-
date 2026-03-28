# Recursion Example: Factorial

# Function to calculate factorial using recursion
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

# Taking a number
num = 5

# Calling the function
result = factorial(num)

# Printing result
print("Factorial of", num, "is:", result)

# Output:
# Factorial of 5 is: 120
