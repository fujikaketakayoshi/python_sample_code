nums = [2, 1, 5, 0, 4, 6, 3, 7, 8, 9]
N = len(nums)
dp = [1] * N

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
