data = [
    (100, 'ABC'),
    (200, 'BCD'),
    (100, 'ABD'),
    (300, 'ACD')
]
# スコアを降順、名前を昇順でソート
data.sort(key=lambda x: (-x[0], x[1]))
print(data)
