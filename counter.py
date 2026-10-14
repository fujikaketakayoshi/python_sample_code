from collections import Counter

words = ["foo", "foo", "bar"]
cnt = Counter(words)
print(cnt)
print(cnt.most_common(1)) # 出現頻度が最も高い要素とその数をタプルで返す
print(cnt['foo'])
print(cnt['bar'])
print(cnt['baz'])  # 存在しないキーは0を返す
cnt['foo'] += 1
print(cnt)
cnt['bar'] += 2
print(cnt)
print(cnt.most_common())

