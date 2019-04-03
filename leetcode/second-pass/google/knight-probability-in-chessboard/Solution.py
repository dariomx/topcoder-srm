class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def neighbors(x, y):
            for dx, dy in ((2, 1), (1, 2)):
                for sx in (-1, +1):
                    for sy in (-1, +1):
                        nx, ny = x + sx * dx, y + sy * dy
                        if (0 <= nx < N and 0 <= ny < N):
                            yield nx, ny

        curr = [[0] * N for _ in range(N)]
        prev = [[1] * N for _ in range(N)]
        for k in range(1, K + 1):
            for i in range(N):
                for j in range(N):
                    curr[i][j] = 0
                    for x, y in neighbors(i, j):
                        curr[i][j] += prev[x][y]
            curr, prev = prev, curr
        return prev[r][c] / (8 ** K)
