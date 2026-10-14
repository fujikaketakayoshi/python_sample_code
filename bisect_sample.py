import bisect

A = [100, 200, 300, 400]
idx = bisect.bisect_left(A, 250)
print(idx)  # Output: 2