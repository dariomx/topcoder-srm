class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        delta = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        queue = [(0, (0, 0))]
        min_dist = [[inf] * n for _ in range(m)]
        ans = inf
        while queue:
            dist, node = heappop(queue)
            if node == (m - 1, n - 1):
                ans = min(ans, dist)
                continue
            x, y = node
            for ndir, dxy in delta.items():
                nx, ny = x + dxy[0], y + dxy[1]
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                ndist = dist + int(grid[x][y] != ndir)
                if ndist < min_dist[nx][ny]:
                    min_dist[nx][ny] = ndist
                    heappush(queue, (ndist, (nx, ny)))
        return ans if ans < inf else -1
