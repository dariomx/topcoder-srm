from collections import defaultdict

class Solution:
    def countCornerRectangles(self, grid):
        n, m = len(grid), len(grid[0])
        lines = defaultdict(lambda: 0)
        cnt = 0
        for x in range(n):
            for start in range(m-1):
                if grid[x][start] == 0:
                    continue
                for end in range(start+1, m):
                    if grid[x][end] == 1:
                        cnt += lines[(start, end)]
                        lines[(start, end)] += 1
        return cnt