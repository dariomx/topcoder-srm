class Solution:
    def getRottenGood(self, grid, queue):
        n, m = len(grid), len(grid[0])
        rotten, good = set(), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append(((i, j), 1))
                    rotten.add((i, j))
                elif grid[i][j] == 1:
                    good += 1
        return rotten, good

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        queue = deque()
        visited, good = self.getRottenGood(grid, queue)
        ans = 0
        while queue and good > 0:
            (i, j), mins = queue.popleft()
            ans = max(ans, mins)
            for ni, nj in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                nei = ni, nj
                if not (0 <= ni < n and 0 <= nj < m) or \
                        nei in visited or grid[ni][nj] == 0:
                    continue
                if grid[ni][nj] == 1 and nei not in visited:
                    visited.add(nei)
                    good -= 1
                queue.append((nei, mins + 1))
        if good == 0:
            return ans
        else:
            return -1