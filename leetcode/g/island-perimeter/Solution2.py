class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        perim = 0
        for x in xrange(n):
            for y in xrange(m):
                if grid[x][y] == 0:
                    continue
                for c in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    i, j = c
                    if 0 <= i < n and 0 <= j < m:
                        perim += 1 - grid[i][j]
                    else:
                        perim += 1
        return perim
