nums = [2, 1, 7, 8, 9, 6, 3, 4, 5, 0]
N = len(nums)
dp = [1] * N

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(max(dp))
