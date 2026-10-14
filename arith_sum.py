def arith_sum(a, l, n):
    return n * (a + l) // 2

print(arith_sum(1, 100, 100))  # 出力: 5050

a = 1
l = 100
print(arith_sum(a, l, l - a + 1))  # 出力: 5050