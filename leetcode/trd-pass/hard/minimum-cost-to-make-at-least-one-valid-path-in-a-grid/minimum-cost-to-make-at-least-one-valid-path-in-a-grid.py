class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([((0, 0), 0)])
        min_dist = defaultdict(lambda: inf)
        delta = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        ans = inf
        while queue:
            node, dist = queue.popleft()
            if node == (m - 1, n - 1):
                ans = min(ans, dist)
                continue
            x, y = node
            for ndir, dxy in delta.items():
                nx, ny = x + dxy[0], y + dxy[1]
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                ndist = dist + int(grid[x][y] != ndir)
                nei = nx, ny
                if ndist < min_dist[nei] and ndist < min_dist[m - 1, n - 1]:
                    min_dist[nei] = ndist
                    queue.append((nei, ndist))
        return ans if ans < inf else -1
