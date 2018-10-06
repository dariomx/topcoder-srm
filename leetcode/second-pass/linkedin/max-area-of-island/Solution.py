class Solution:
    def dfs(self, start, n, m, grid, visited):
        area = 0
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            area += 1
            x, y = node
            for nei in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                i, j = nei
                if not (0 <= i < n and 0 <= j < m):
                    continue
                if grid[i][j] == 1:
                    stack.append(nei)
        return area

    def maxAreaOfIsland(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        visited = set()
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = self.dfs((i, j), n, m, grid, visited)
                    maxArea = max(maxArea, area)
        return maxArea
