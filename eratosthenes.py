import math

N = 1000
# エラトステネスの篩
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for p in range(2, math.isqrt(N) + 1):
    if is_prime[p]:
        for j in range(p * p, N + 1, p):
            is_prime[j] = False
primes = []
for p in range(2, N + 1):
  if is_prime[p]:
    primes.append(p)
print(primes)  # 最初の10個の素数を表示