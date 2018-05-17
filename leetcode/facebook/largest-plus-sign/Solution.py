class Solution:
    def get_grid(self, N, mines):
        grid = [[1] * N for _ in range(N)]
        for i, j in mines:
            grid[i][j] = 0
        return grid

    def get_left(self, N, grid):
        left = [[0] * N for _ in range(N)]
        for i in range(N):
            left[i][0] = grid[i][0]
            for j in range(1, N):
                if grid[i][j] > 0:
                    left[i][j] = 1 + left[i][j - 1]
        return left

    def get_right(self, N, grid):
        right = [[0] * N for _ in range(N)]
        for i in range(N):
            right[i][N - 1] = grid[i][N - 1]
            for j in range(N - 2, -1, -1):
                if grid[i][j] > 0:
                    right[i][j] = 1 + right[i][j + 1]
        return right

    def get_up(self, N, grid):
        up = [[0] * N for _ in range(N)]
        for j in range(N):
            up[0][j] = grid[0][j]
            for i in range(1, N):
                if grid[i][j] > 0:
                    up[i][j] = 1 + up[i - 1][j]
        return up

    def get_down(self, N, grid):
        down = [[0] * N for _ in range(N)]
        for j in range(N):
            down[N - 1][j] = grid[N - 1][j]
            for i in range(N - 2, -1, -1):
                if grid[i][j] > 0:
                    down[i][j] = 1 + down[i + 1][j]
        return down

    def orderOfLargestPlusSign(self, N, mines):
        grid = self.get_grid(N, mines)
        left = self.get_left(N, grid)
        right = self.get_right(N, grid)
        up = self.get_up(N, grid)
        down = self.get_down(N, grid)
        max_order = 0
        for i in range(N):
            for j in range(N):
                order = min(left[i][j], right[i][j], up[i][j], down[i][j])
                max_order = max(max_order, order)
        return max_order
