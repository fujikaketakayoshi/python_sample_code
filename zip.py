a = [1, 2, 3, 4]
b = [4, 5, 6]
c = list(zip(a, b))
print(c)

for x, y in zip(a, b):
    print(x, y)
