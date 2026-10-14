n, m = 2, 3
arr = [False] * n
print(arr)
arr2 = [arr for _ in range(m)]
print(arr2)

arr3 = [[False] * n for _ in range(m)]
print(arr3)
