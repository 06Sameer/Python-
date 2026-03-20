# BASIC OPERATIONS USING WHILE LOOP


# 1. Print numbers from 1 to 5
i = 1
while i <= 5:
    print("Number:", i)
    i += 1

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5


# -------------------------------

# 2. Sum of first 5 natural numbers
i = 1
sum = 0

while i <= 5:
    sum += i
    i += 1

print("Sum:", sum)

# Output:
# Sum: 15


# -------------------------------

# 3. Print even numbers from 1 to 10
i = 1

while i <= 10:
    if i % 2 == 0:
        print("Even:", i)
    i += 1

# Output:
# Even: 2
# Even: 4
# Even: 6
# Even: 8
# Even: 10


# -------------------------------

# 4. Reverse a number using while loop
num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed Number:", rev)

# Output:
# Reversed Number: 4321


# -------------------------------

# 5. Multiplication table of 5
i = 1

while i <= 10:
    print("5 x", i, "=", 5 * i)
    i += 1

# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50


# -------------------------------

# 6. Infinite loop with break condition
i = 1

while True:
    print("Count:", i)
    if i == 5:
        break
    i += 1

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5


# -------------------------------

# 7. Skip numbers using continue
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print("Value:", i)

# Output:
# Value: 1
# Value: 2
# Value: 4
# Value: 5
