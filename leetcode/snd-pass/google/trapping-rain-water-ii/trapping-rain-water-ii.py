from math import inf
from collections import defaultdict


class Solution:
    def neighbors(self, x, y, hmap):
        m, n = len(hmap), len(hmap[0])
        for dx, dy in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                yield nx, ny

    def isEdge(self, x, y, hmap):
        m, n = len(hmap), len(hmap[0])
        return x in (0, m - 1) or y in (0, n - 1)

    def dfs(self, start, visited, level, hmap):
        island = []
        stack = [start]
        min_h = inf
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            x, y = node
            if self.isEdge(x, y, hmap):
                min_h = 0
            visited.add(node)
            island.append(node)
            for nx, ny in self.neighbors(x, y, hmap):
                if hmap[nx][ny] == level:
                    stack.append((nx, ny))
                else:
                    min_h = min(min_h, hmap[nx][ny])
        if min_h == inf:
            min_h = 0
        return island, min_h

    def groupByLevel(self, hmap):
        levels = defaultdict(list)
        m, n = len(hmap), len(hmap[0])
        for i in range(m):
            for j in range(n):
                levels[hmap[i][j]].append((i, j))
        return levels

    def trapRainWater(self, hmap: List[List[int]]) -> int:
        levels = self.groupByLevel(hmap)
        ans = 0
        for lev in sorted(levels.keys()):
            visited = set()
            for start in levels[lev]:
                if start in visited:
                    continue
                island, min_h = self.dfs(start, visited, lev, hmap)
                for x, y in island:
                    ans += max(min_h - lev, 0)
                    hmap[x][y] = min_h
                    levels[lev].append((x, y))
        return ans
