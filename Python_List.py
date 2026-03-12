# Performing basic operations on a list in Python

# Creating a list
list = [10, 20, 30, 40]

# Print list
print("Original List:", list)

# Add element (append)
list.append(50)
print("After Adding 50:", list)

# Insert element at specific position
list.insert(2, 25)
print("After Inserting 25 at index 2:", list)

# Remove element
list.remove(30)
print("After Removing 30:", list)

# Pop element (remove by index)
list.pop(1)
print("After Pop at index 1:", list)

# Update element
list[2] = 100
print("After Updating index 2 to 100:", list)

# Length of list
print("Length of list:", len(list))

# Searching element
if 40 in list:
    print("40 is present in the list")
else:
    print("40 is not present in the list")

# Sorting list
list.sort()
print("Sorted List:",list)

# Reversing list
list.reverse()
print("Reversed List:", list)
