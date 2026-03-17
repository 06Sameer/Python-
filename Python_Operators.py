# Demonstration of Operator Precedence in Python

# Example 1
result1 = 10 + 5 * 2
print("10 + 5 * 2 =", result1)  
# Multiplication (*) has higher precedence than addition (+)

# Example 2
result2 = (10 + 5) * 2
print("(10 + 5) * 2 =", result2)  
# Parentheses () have highest precedence

# Example 3
result3 = 20 - 4 / 2
print("20 - 4 / 2 =", result3)  
# Division (/) happens before subtraction (-)

# Example 4
result4 = 2 ** 3 * 2
print("2 ** 3 * 2 =", result4)  
# Exponentiation (**) has higher precedence than multiplication (*)

# Example 5
result5 = 100 / 5 + 3 * 2
print("100 / 5 + 3 * 2 =", result5)  
# Division and multiplication happen before addition

# Example 6
result6 = 5 + 2 * 3 ** 2
print("5 + 2 * 3 ** 2 =", result6)  
# Order: ** → * → +

# Example 7 (Using all together)
result7 = (5 + 2) * 3 ** 2 - 4 / 2
print("(5 + 2) * 3 ** 2 - 4 / 2 =", result7)

# Summary print
print("\nOperator Precedence Order:")
print("1. Parentheses ()")
print("2. Exponentiation **")
print("3. Multiplication *, Division /, Modulus %")
print("4. Addition +, Subtraction -")
