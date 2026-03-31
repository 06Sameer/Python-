from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() → change each value
result_map = list(map(lambda x: x + 1, numbers))
print(result_map)
# Output: [2, 3, 4, 5, 6]


# filter() → select values
result_filter = list(filter(lambda x: x > 2, numbers))
print(result_filter)
# Output: [3, 4, 5]


# reduce() → combine values
result_reduce = reduce(lambda x, y: x + y, numbers)
print(result_reduce)
# Output: 15
