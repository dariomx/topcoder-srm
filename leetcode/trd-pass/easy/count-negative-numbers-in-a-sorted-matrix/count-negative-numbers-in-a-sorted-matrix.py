class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        col = 0
        ans = 0
        for i in reversed(range(m)):
            if grid[i][n - 1] > 0:
                break
            elif grid[i][0] < 0:
                ans += n
            else:
                for j in reversed(range(col, n)):
                    if grid[i][j] < 0:
                        ans += 1
                    else:
                        col = j
                        break
        return ans
