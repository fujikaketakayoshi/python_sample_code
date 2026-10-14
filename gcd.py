def gcd(a, b):
    while b:
        a, b = b, a % b
        print(a, b)
    return a

print(gcd(48, 18))  # Output: 6
print(gcd(56, 98))  # Output: 14
print(gcd(101, 10))  # Output: 1
