from collections import defaultdict

cnt = defaultdict(int)
cnt1 = defaultdict(lambda: defaultdict(int))

cnt['a'] += 1
cnt['b'] += 2
cnt['a'] += 3
print(cnt)  # 出力: defaultdict(<class 'int'>, {'a': 4, 'b': 2})
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[0][0])

