class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def rec(prod, i, j):
            if i == m or j == n:
                return prod
            prod *= grid[i][j]
            if i == m - 1:
                return rec(prod, i, j+1)
            elif j == n - 1:
                return rec(prod, i+1, j)
            else:
                return max(rec(prod, i, j+1), rec(prod, i+1, j))

        ans = rec(1, 0, 0)
        return ans % (10**9 + 7) if ans >= 0 else -1
