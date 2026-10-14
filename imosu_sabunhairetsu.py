n = 10

# 差分配列（1つ余分に確保）
diff = [0] * (n + 1)

# 区間 [2,5] に +3
diff[2] += 3
diff[6] -= 3   # 5の次で止める

# 区間 [4,8] に +2
diff[4] += 2
diff[9] -= 2   # 8の次で止める

# 累積和で元の配列を復元
a = [0] * n
a[0] = diff[0]
for i in range(1, n):
    a[i] = a[i-1] + diff[i]

print(a)
