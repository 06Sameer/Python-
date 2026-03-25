# Python Return Function Examples


# -------------------------------
# 1. Square of a number
def square(n):
    return n * n


# 2. Find maximum of two numbers
def find_max(a, b):
    if a > b:
        return a
    return b


# 3. Factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# 4. Reverse a string
def reverse_string(text):
    return text[::-1]


# 5. Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# 6. Get even numbers from a list
def get_even_numbers(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result


# 7. Return multiple values (sum & product)
def calculate(a, b):
    return a + b, a * b


# 8. Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 9. Early return example
def check_number(n):
    if n < 0:
        return "Negative"
    return "Positive"


# 10. Simple login system
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    return "Invalid Credentials"


# -------------------------------
# Main Execution
if __name__ == "__main__":
    print("----- Function Outputs -----\n")

    print("1. Square:", square(4))  # Output: 16
    print("2. Max:", find_max(10, 25))  # Output: 25
    print("3. Factorial:", factorial(5))  # Output: 120
    print("4. Reverse:", reverse_string("python"))  # Output: nohtyp
    print("5. Vowels:", count_vowels("Hello World"))  # Output: 3
    print("6. Even Numbers:", get_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]

    sum_val, product_val = calculate(3, 4)
    print("7. Sum:", sum_val, "| Product:", product_val)  # Output: 7 | 12

    print("8. Is Prime (7):", is_prime(7))  # Output: True
    print("9. Check Number (-5):", check_number(-5))  # Output: Negative
    print("10. Login:", login("admin", "1234"))  # Output: Login Successful
