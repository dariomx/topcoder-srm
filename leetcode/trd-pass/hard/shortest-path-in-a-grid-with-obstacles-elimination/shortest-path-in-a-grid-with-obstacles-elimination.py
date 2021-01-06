class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        queue = deque([(0, 0, k, 0)])
        visited = {(0, 0, k)}
        while queue:
            x, y, obst, dist = queue.popleft()
            if (x, y) == (n - 1, m - 1):
                return dist
            else:
                for dx, dy in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                    nx, ny = x + dx, y + dy
                    key = (nx, ny, obst)
                    if not (0 <= nx < n and 0 <= ny < m) or key in visited:
                        continue
                    if grid[nx][ny] == 0:
                        visited.add(key)
                        queue.append((nx, ny, obst, dist + 1))
                    elif grid[nx][ny] == 1 and obst > 0:
                        visited.add(key)
                        queue.append((nx, ny, obst - 1, dist + 1))
        return -1
