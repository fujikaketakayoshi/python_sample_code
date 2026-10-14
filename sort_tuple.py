A = [(28, -7), (8, -17), (-21, -17), (10, -15), (-19, -15), (-6, -5)]
# 普通に昇順
sorted(A)
print(sorted(A))

# 降順
sorted(A, reverse=True)
print(sorted(A, reverse=True))

# タプルの2番目でソート
sorted(A, key=lambda x: x[1])
print(sorted(A, key=lambda x: x[1]))

# タプルの2番目を降順
sorted(A, key=lambda x: x[1], reverse=True)
print(sorted(A, key=lambda x: x[1], reverse=True))

# 2番目昇順 → 同じなら1番目昇順
sorted(A, key=lambda x: (x[1], x[0]))
print(sorted(A, key=lambda x: (x[1], x[0])))

# 1番目昇順 → 同じなら2番目降順
sorted(A, key=lambda x: (x[0], -x[1]))
print(sorted(A, key=lambda x: (x[0], -x[1])))