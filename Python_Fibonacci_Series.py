# Recursion Example: Fibonacci Series

# Function to find nth Fibonacci number
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)


# Print first 10 Fibonacci numbers
print("Fibonacci Series:")

for i in range(10):
    print(fibonacci(i), end=" ")

# Output:
# Fibonacci Series:
# 0 1 1 2 3 5 8 13 21 34
