class Solution:
    def calc_left(self, left, N, grid):
        for i in range(N):
            cnt = 0
            for j in range(N):
                if grid[i][j] == 0:
                    cnt = 0
                else:
                    cnt += 1
                    left[i][j] = cnt

    def calc_right(self, right, N, grid):
        for i in range(N):
            cnt = 0
            for j in range(N - 1, -1, -1):
                if grid[i][j] == 0:
                    cnt = 0
                else:
                    cnt += 1
                    right[i][j] = min(right[i][j], cnt)

    def calc_up(self, up, N, grid):
        for j in range(N):
            cnt = 0
            for i in range(N):
                if grid[i][j] == 0:
                    cnt = 0
                else:
                    cnt += 1
                    up[i][j] = min(up[i][j], cnt)

    def calc_down(self, down, N, grid):
        for j in range(N):
            cnt = 0
            for i in range(N - 1, -1, -1):
                if grid[i][j] == 0:
                    cnt = 0
                else:
                    cnt += 1
                    down[i][j] = min(down[i][j], cnt)

    def orderOfLargestPlusSign(self, N, mines):
        grid = [[1] * N for _ in range(N)]
        for i, j in mines:
            grid[i][j] = 0
        cnt = [[0] * N for _ in range(N)]
        self.calc_left(cnt, N, grid)
        self.calc_right(cnt, N, grid)
        self.calc_up(cnt, N, grid)
        self.calc_down(cnt, N, grid)
        max_order = 0
        for i in range(N):
            for j in range(N):
                max_order = max(max_order, cnt[i][j])
        return max_order
