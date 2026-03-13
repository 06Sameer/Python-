# Tuple Operations in Python

# Creating Tuples
t1 = (10, 20, 30, 40, 50)
t2 = ("apple", "banana", "mango")
t3 = (1, 2, 3, 4, 5)

print("Tuple 1:", t1)
print("Tuple 2:", t2)

# Accessing Elements (Indexing)
print("First element of t1:", t1[0])
print("Last element of t1:", t1[-1])

# Slicing
print("Elements from index 1 to 3:", t1[1:4])

# Tuple Length
print("Length of t1:", len(t1))

# Concatenation
t4 = t1 + t3
print("Concatenated Tuple:", t4)

# Repetition
t5 = t2 * 2
print("Repeated Tuple:", t5)

# Membership Test
print("Is 20 present in t1?", 20 in t1)
print("Is 'apple' present in t2?", "apple" in t2)

# Iterating through Tuple
print("Elements in t1:")
for i in t1:
    print(i)

# Count Method
t6 = (1, 2, 2, 3, 4, 2, 5)
print("Count of 2 in tuple:", t6.count(2))

# Index Method
print("Index of 3 in tuple:", t6.index(3))

# Converting List to Tuple
list1 = [100, 200, 300]
tuple_from_list = tuple(list1)
print("Tuple from list:", tuple_from_list)

# Nested Tuple
nested_tuple = (1, (2, 3), (4, 5))
print("Nested Tuple:", nested_tuple)
print("Access nested element:", nested_tuple[1][0])

# Tuple Packing
packed = 10, 20, 30
print("Packed Tuple:", packed)

# Tuple Unpacking
a, b, c = packed
print("Unpacked values:", a, b, c)
