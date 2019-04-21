from collections import defaultdict

START = 0
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4
dirs = {UP: (0, +1), RIGHT: (+1, 0), DOWN: (-1, 0), LEFT: (0, -1)}


class Solution:
    def dfs(self, start, visited, grid):
        n, m = len(grid), len(grid[0])
        path = []
        stack = [(start, (0, 0))]
        while stack:
            node, rxy = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            path.append(rxy)
            for d in dirs:
                dx, dy = dirs[d]
                x, y = node[0] + dx, node[1] + dy
                rx, ry = rxy[0] + dx, rxy[1] + dy
                if not (0 <= x < n and 0 <= y < m) or grid[x][y] == 0:
                    continue
                stack.append(((x, y), (rx, ry)))
        return tuple(path)

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = defaultdict(lambda: set())
        n, m = len(grid), len(grid[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    path = self.dfs((i, j), visited, grid)
                    if len(path) > 0:
                        islands[len(path)].add(path)
        return sum((len(islands[i]) for i in islands))