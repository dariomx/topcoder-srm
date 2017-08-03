from collections import deque
from sys import maxint


class Solution(object):
    def bfs(self, start, grid, queue, visited):
        n, m = len(grid), len(grid[0])
        queue.clear()
        visited.clear()
        queue.append((start, 0))
        visited.add(start)
        build_dist = 0
        num_build = 0
        while queue:
            (x, y), dist = queue.popleft()
            if grid[x][y] == 1:
                build_dist += dist
                num_build += 1
            else:
                for (i, j) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= i < n and 0 <= j < m and \
                                    grid[i][j] != 2 and (i, j) not in visited:
                        visited.add((i, j))
                        queue.append(((i, j), dist + 1))
        return build_dist, num_build

    def count_buildings(self, grid):
        cnt = 0
        n, m = len(grid), len(grid[0])
        for x in xrange(n):
            for y in xrange(m):
                if grid[x][y] == 1:
                    cnt += 1
        return cnt

    def shortestDistance(self, grid):
        n = len(grid)
        if n > 0:
            m = len(grid[0])
        if 0 in (n, m):
            return 0
        queue = deque()
        visited = set()
        min_dist = maxint
        total_build = self.count_buildings(grid)
        for x in xrange(n):
            for y in xrange(m):
                if grid[x][y] == 0:
                    build_dist, num_build = \
                        self.bfs((x, y), grid, queue, visited)
                    if num_build == total_build:
                        min_dist = min(min_dist, build_dist)
        return min_dist if min_dist < maxint else -1
