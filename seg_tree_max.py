class SegTree:
    def __init__(self, A):
        n = len(A)

        self.size = 1
        while self.size < n:
            self.size *= 2

        self.data = [float("-inf")] * (self.size * 2)

        for i in range(n):
            self.data[self.size + i] = A[i]

        for i in range(self.size - 1, 0, -1):
            self.data[i] = max(
                self.data[i * 2],
                self.data[i * 2 + 1]
            )

    def update(self, i, value):
        i += self.size
        self.data[i] = value

        while i > 1:
            i //= 2
            self.data[i] = max(
                self.data[i * 2],
                self.data[i * 2 + 1]
            )

    def query(self, l, r):
        l += self.size
        r += self.size

        ans = float("-inf")

        while l < r:
            if l % 2 == 1:
                ans = max(ans, self.data[l])
                l += 1

            if r % 2 == 1:
                r -= 1
                ans = max(ans, self.data[r])

            l //= 2
            r //= 2

        return ans

P = [5, 2, 3, 1, 6]
N = len(P)

seg = SegTree(P)

print(seg.query(1, N))
