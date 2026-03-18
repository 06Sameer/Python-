# Python Program to Demonstrate if, elif, else Conditions

# Example 1: Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


# Example 2: Check voting eligibility
age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Example 3: Grade calculator
marks = int(input("\nEnter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


# Example 4: Check largest of three numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
