from itertools import product

print(tuple(product(range(3), repeat=3)))

N = 5
nums = list(range(1, N + 1))
print(nums)
print(tuple(product(nums, repeat=N)))
