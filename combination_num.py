N = 3
K = 2
def combination_num(n, k):
    if k == 0 or k == n:
        return 1
    return combination_num(n - 1, k - 1) + combination_num(n - 1, k)
print(combination_num(N, K))
import math

N = 2 * 10 ** 5 - 1
K = 2
print(math.comb(N, K))
