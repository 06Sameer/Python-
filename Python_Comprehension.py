# LIST COMPREHENSION

# 1. Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)
# Output: Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 2. Get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)
# Output: Even Numbers: [2, 4, 6]


# 3. Convert list to uppercase
words = ["python", "data", "science"]
upper_words = [word.upper() for word in words]
print("Uppercase Words:", upper_words)
# Output: Uppercase Words: ['PYTHON', 'DATA', 'SCIENCE']


# SET COMPREHENSION

# 4. Create a set of unique squares
nums = [1, 2, 2, 3, 4, 4]
unique_squares = {x**2 for x in nums}
print("Unique Squares:", unique_squares)
# Output: Unique Squares: {16, 1, 4, 9}


# 5. Filter vowels from a string
text = "hello world"
vowels = {char for char in text if char in "aeiou"}
print("Vowels:", vowels)
# Output: Vowels: {'e', 'o'}


# DICTIONARY COMPREHENSION

# 6. Create a dictionary of numbers and their squares
square_dict = {x: x**2 for x in range(1, 6)}
print("Square Dictionary:", square_dict)
# Output: Square Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 7. Filter dictionary (only even values)
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_dict = {k: v for k, v in original_dict.items() if v % 2 == 0}
print("Filtered Dictionary:", even_dict)
# Output: Filtered Dictionary: {'b': 2, 'd': 4}


# NESTED COMPREHENSION

# 8. Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print("Flattened List:", flattened)
# Output: Flattened List: [1, 2, 3, 4, 5, 6]


# 9. Create multiplication table (1 to 3)
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplication Table:", table)
# Output: Multiplication Table: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
