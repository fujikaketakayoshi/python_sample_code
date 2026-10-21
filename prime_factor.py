def prime_factor_list(n):
    res = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            res.append(d)
            n //= d
        d += 1
    if n > 1:
        res.append(n)
    return res

print(prime_factor_list(60))  # 出力: [2, 2, 3, 5]
print(prime_factor_list(6))
print(prime_factor_list(8))

def prime_factors(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

print(prime_factors(60))  # 出力: {2: 2, 3: 1, 5: 1}