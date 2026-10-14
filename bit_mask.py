mask = 10
N = 5
i = 2

print(bin(mask))
print(bin(1 << i))
print(bin(mask >> i))
print(bin((mask >> i) & 1))
print(bin(mask | (1 << i)))
print(bin((1 << N) - 1))
