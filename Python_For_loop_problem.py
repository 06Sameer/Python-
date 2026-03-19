# FIND PRIME NUMBERS IN A RANGE

start = 1
end = 20

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break  # not prime
        else:
            print(num)

# Output:
# Prime numbers between 1 and 20 are:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
