class PrefixSum2D:
    def __init__(self, grid):
        H = len(grid)
        W = len(grid[0])

        self.ps = [[0] * (W + 1) for _ in range(H + 1)]

        for y in range(H):
            for x in range(W):
                self.ps[y + 1][x + 1] = (
                    self.ps[y][x + 1]
                    + self.ps[y + 1][x]
                    - self.ps[y][x]
                    + grid[y][x]
                )

    def sum(self, top, left, bottom, right):
        return (
            self.ps[bottom + 1][right + 1]
            - self.ps[top][right + 1]
            - self.ps[bottom + 1][left]
            + self.ps[top][left]
        )

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

ps = PrefixSum2D(grid)

print(ps.sum(0, 0, 1, 1))  # 1+2+4+5 = 12
print(ps.sum(1, 1, 2, 2))  # 5+6+8+9 = 28