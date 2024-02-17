def multiply(*nums):
    total_value = 1
    for el in nums:
        total_value *= el
    return total_value

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))