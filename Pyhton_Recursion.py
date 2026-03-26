# RECURSION EXAMPLES

# Print numbers from 1 to 5
def print_numbers(n):
    if n > 5:   # Base case
        return
    print(n, end=" ")
    print_numbers(n + 1)

print("1. Print Numbers:")
print_numbers(1)
print("\n")
# Output:
# 1 2 3 4 5


# Factorial of a number
def factorial(n):
    if n == 1:   # Base case
        return 1
    return n * factorial(n - 1)

print("2. Factorial of 5:")
print(factorial(5))
print()
# Output:
# 120


# Sum of first n natural numbers
def sum_n(n):
    if n == 1:   # Base case
        return 1
    return n + sum_n(n - 1)

print("3. Sum of first 5 numbers:")
print(sum_n(5))
print()
# Output:
# 15


# Reverse a string
def reverse_string(s):
    if len(s) == 0:   # Base case
        return s
    return reverse_string(s[1:]) + s[0]

print("4. Reverse string:")
print(reverse_string("hello"))
print()
# Output:
# olleh


# Fibonacci (nth term)
def fibonacci(n):
    if n == 0:   # Base case
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("5. Fibonacci (6th term):")
print(fibonacci(6))
print()
# Output:
# 8
