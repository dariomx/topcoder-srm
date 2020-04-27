class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        else:
            m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        def dfs(x, y):
            if visited[x][y]:
                return
            visited[x][y] = True
            for delta in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                nx, ny = x + delta[0], y + delta[1]
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                    dfs(nx, ny)
        ans = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '1' and not visited[x][y]:
                    dfs(x, y)
                    ans += 1
        return ans