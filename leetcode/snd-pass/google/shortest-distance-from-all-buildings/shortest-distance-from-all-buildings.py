# kinda resurrected soln read time ago

from collections import deque
from math import inf


class Solution:
    def init_dist(self, grid):
        dist = dict()
        build = []
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dist[i, j] = dict()
                elif grid[i][j] == 1:
                    build.append((i, j))
        return dist, build

    def neighbors(self, pos, grid):
        x, y = pos
        n, m = len(grid), len(grid[0])
        for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= i < n and 0 <= j < m and grid[i][j] == 0:
                yield i, j

    def bfs(self, start, grid, dist):
        queue = deque([(start, 0)])
        used = set()
        while queue:
            node, d = queue.popleft()
            x, y = node
            if grid[x][y] == 0:
                dist[node][start] = d
            for nei in self.neighbors(node, grid):
                if nei in used:
                    continue
                used.add(nei)
                queue.append((nei, d + 1))

    def shortestDistance(self, grid: List[List[int]]) -> int:
        dist, build = self.init_dist(grid)
        for start in build:
            self.bfs(start, grid, dist)
        ans = inf
        for empty in dist:
            if len(dist[empty]) == len(build):
                ans = min(ans, sum(dist[empty].values()))
        return -1 if ans == inf else ans
