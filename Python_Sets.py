# Basic Set Operations in Python

# Creating a set
fruits = {"apple", "banana", "mango", "orange"}
print("Original Set:", fruits)

# Adding an element
fruits.add("grapes")
print("After add():", fruits)

# Removing an element
fruits.remove("banana")
print("After remove():", fruits)

# Discarding an element (does not give error if element not present)
fruits.discard("pineapple")
print("After discard():", fruits)

# Copying a set
new_fruits = fruits.copy()
print("Copied Set:", new_fruits)

# Clearing the set
temp_set = {"a", "b", "c"}
temp_set.clear()
print("After clear():", temp_set)

# Set Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1.union(set2))

# Set Intersection
print("Intersection:", set1.intersection(set2))

# Set Difference
print("Difference (set1 - set2):", set1.difference(set2))

# Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Checking subset
A = {1, 2}
B = {1, 2, 3, 4}
print("Is A subset of B?", A.issubset(B))

# Checking superset
print("Is B superset of A?", B.issuperset(A))
