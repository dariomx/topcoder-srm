class Solution:
    def getStartEnd(self, grid):
        n, m = len(grid), len(grid[0])
        start, end, tot_zeros = None, None, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    tot_zeros += 1
                elif grid[i][j] == 1:
                    start = i, j
                elif grid[i][j] == 2:
                    end = i, j
        return start, end, tot_zeros

    def neighbors(self, xy, grid):
        n, m = len(grid), len(grid[0])
        x, y = xy
        for dx, dy in ((0, +1), (0, -1), (+1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] >= 0:
                yield nx, ny

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start, end, tot_zeros = self.getStartEnd(grid)
        used = {start}
        ans = 0

        def search(node):
            nonlocal ans
            if node == end:
                if len(used) - 2 == tot_zeros:
                    ans += 1
            else:
                for nei in self.neighbors(node, grid):
                    if nei not in used:
                        used.add(nei)
                        search(nei)
                        used.remove(nei)

        search(start)
        return ans
