ans = [1, 2, 3]
print(*ans)

grid = [
    [1, 2, 3],
    [4, 5, 6]
]

vertical = list(zip(*grid))
print(vertical)

transposed = [list(row) for row in zip(*grid)]
print(transposed)



def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))
