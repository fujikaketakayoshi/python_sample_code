class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        # [0, i)
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l)

    def lower_bound(self, w):
        """
        sum(idx) >= w となる最小 idx を返す
        """
        if w <= 0:
            return 0

        x = 0
        k = 1 << (self.n.bit_length() - 1)

        while k:
            if x + k <= self.n and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k >>= 1

        return x

bit = BIT(10)
bit.add(0, 1)
bit.add(1, 1)
bit.add(2, 2)
bit.add(3, 3)
bit.add(9, 4)
print(bit.sum(4))  # 出力: 6 (1 + 2 + 3)
print(bit.sum(3))  # 出力: 3 (1 + 2)
print(bit.sum(2))  # 出力: 1 (1)
print(bit.sum(1))  # 出力: 0 ()
# print(bit.sum(11)) # out of range
print(bit.sum(10))
print(bit.range_sum(1, 3))  # 出力: 3 (1 + 2) rの3は含まれない
print(bit.lower_bound(4))  # 出力: 3 (sum(3) = 6 >= 4, sum(2) = 3 < 4)

exit()


#  BITのインデックスの動きの確認

n = 15
for i in range(n):
    idx = i + 1
    print(i + 1, idx)
    while idx <= n:
        idx += idx & -idx
        print(i + 1, idx)

for i in range(n):
    idx = i + 1
    print(i + 1, idx)
    while idx > 0:
        idx -= idx & -idx
        print(i + 1, idx)

