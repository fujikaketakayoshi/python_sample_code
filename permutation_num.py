def permutation_num(n, k):
	if k > n:
		return 0
	result = 1
	for i in range(n, n - k, -1):
		result *= i
	return result


N = 12
K = 12

print(permutation_num(N, K))
