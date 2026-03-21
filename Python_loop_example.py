# Find second largest number in a list

numbers = [10, 25, 8, 40, 30]

largest = numbers[0]
second_largest = numbers[0]

# First loop to find the largest number
for num in numbers:
    if num > largest:
        largest = num

# Second loop to find second largest
for num in numbers:
    if num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)

# Output:
# Largest: 40
# Second Largest: 30
