class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_row = [0] * n
        max_col = [0] * m
        for i in range(n):
            for j in range(m):
                max_row[i] = max(max_row[i], grid[i][j])
                max_col[j] = max(max_col[j], grid[i][j])
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += min(max_row[i], max_col[j]) - grid[i][j]
        return ans
