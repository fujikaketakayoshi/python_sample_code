def subsets_bit(N):
  points = list(range(N))
  subsets = []
  for S in range(1 << N):     # 0 ~ 7
    subset = []
    for i in range(N):     # 各ビットを見る
      if (S >> i) & 1:   # i番目のビットが1なら
        subset.append(points[i])
      subsets.append(subset)
  return subsets

print(subsets_bit(3))  # [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]
