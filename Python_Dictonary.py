# Basic Dictionary Operations in Python

# 1. Creating a dictionary
student = {
    "name": "Sameer",
    "age": 20,
    "course": "Data Science"
}

print("Original Dictionary:")
print(student)

# 2. Accessing values
print("\nAccessing Values:")
print("Name:", student["name"])
print("Age:", student.get("age"))

# 3. Adding a new key-value pair
student["city"] = "Jabalpur"
print("\nAfter Adding City:")
print(student)

# 4. Updating a value
student["age"] = 21
print("\nAfter Updating Age:")
print(student)

# 5. Removing an element using pop()
student.pop("course")
print("\nAfter Removing 'course':")
print(student)

# 6. Removing the last inserted item using popitem()
student.popitem()
print("\nAfter popitem():")
print(student)

# 7. Adding multiple items using update()
student.update({"course": "CSE-DS", "year": "4th Sem"})
print("\nAfter Update:")
print(student)

# 8. Getting all keys
print("\nKeys:")
print(student.keys())

# 9. Getting all values
print("\nValues:")
print(student.values())

# 10. Getting all key-value pairs
print("\nItems:")
print(student.items())

# 11. Checking if key exists
print("\nCheck if 'name' exists:")
if "name" in student:
    print("Key exists")

# 12. Copying a dictionary
student_copy = student.copy()
print("\nCopied Dictionary:")
print(student_copy)

# 13. Clearing the dictionary
student.clear()
print("\nAfter Clearing Dictionary:")
print(student)
