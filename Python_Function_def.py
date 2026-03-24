# BASIC FUNCTION IN PYTHON

# 1. Simple function (no parameters)
def greet():
    print("Hello, welcome to Python functions!")

greet()  
# Output: Hello, welcome to Python functions!


# 2. Function with parameters
def greet_user(name):
    print("Hello", name)

greet_user("Sameer")
# Output: Hello Sameer


# 3. Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)
# Output: Sum: 8


# 4. Function with default parameter
def greet_default(name="Guest"):
    print("Hello", name)

greet_default()
# Output: Hello Guest

greet_default("Rahul")
# Output: Hello Rahul


# 5. Function with multiple return values
def operations(a, b):
    return a + b, a - b, a * b

sum_val, diff_val, mul_val = operations(10, 5)

print("Sum:", sum_val)
print("Difference:", diff_val)
print("Multiplication:", mul_val)

# Output:
# Sum: 15
# Difference: 5
# Multiplication: 50


# 6. Function using condition
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))
# Output: Odd


# 7. Function inside another function (Nested Function)
def outer_function():
    def inner_function():
        return "This is inner function"
    return inner_function()

print(outer_function())
# Output: This is inner function

