# BASIC FOR LOOP OPERATIONS

# Example 1: Print numbers from 1 to 5
print("Print numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# Output:
# Print numbers from 1 to 5:
# 1
# 2
# 3
# 4
# 5


# Example 2: Iterate through a list
print("\nIterate through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# Iterate through a list:
# apple
# banana
# cherry


# Example 3: Iterate through a string
print("\nIterate through a string:")
for char in "Python":
    print(char)

# Output:
# Iterate through a string:
# P
# y
# t
# h
# o
# n


# Example 4: Using break (stop loop early)
print("\nFor loop with break:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Output:
# For loop with break:
# 1
# 2
# 3
# 4


# Example 5: Using continue (skip iteration)
print("\nFor loop with continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:
# For loop with continue:
# 1
# 2
# 4
# 5


# Example 6: Using else with for loop
print("\nFor loop with else:")
for i in range(1, 4):
    print(i)
else:
    print("Loop finished successfully!")

# Output:
# For loop with else:
# 1
# 2
# 3
# Loop finished successfully!


# Example 7: Nested for loop (pattern)
print("\nNested for loop pattern:")
for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()

# Output:
# Nested for loop pattern:
# * * *
# * * *
# * * *


# Example 8: Sum of numbers using for loop
print("\nSum of numbers from 1 to 5:")
total = 0
for i in range(1, 6):
    total += i
print("Sum =", total)

# Output:
# Sum of numbers from 1 to 5:
# Sum = 15


# Example 9: Multiplication table of 5
print("\nMultiplication table of 5:")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# Output:
# Multiplication table of 5:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
