class Solution(object):
    def get_start(self, grid, n, m):
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    return (i, j)
        return None

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
        start = self.get_start(grid, n, m)
        if start is None:
            return 0
        stack = [start]
        visited = set()
        perim = 0
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            x, y = node
            for c in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                i, j = c
                if 0 <= i < n and 0 <= j < m:
                    perim += 1 - grid[i][j]
                stack.append(c)
        return perim