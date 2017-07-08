class Solution(object):
    def getNeighbors(self, node, grid):
        x, y = node
        n, m = len(grid), len(grid[0])
        for (i, j) in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < n and 0 <= j < m and grid[i][j] == '1':
                yield (i, j)

    def dfsVisit(self, start, grid, visited):
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for n in self.getNeighbors(node, grid):
                stack.append(n)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n > 0:
            m = len(grid[0])
        if n == 0 or m == 0:
            return 0
        cnt = 0
        visited = set()
        for x in xrange(n):
            for y in xrange(m):
                node = (x, y)
                if grid[x][y] == '1' and node not in visited:
                    cnt += 1
                    self.dfsVisit(node, grid, visited)
        return cnt

grid = ["11110","11010","11000","00000"]
print(Solution().numIslands(grid))