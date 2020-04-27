# Simplified version after seeing other's soln

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int],
                dest: List[int]) -> bool:
        n, m = len(maze), len(maze[0])
        dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        stack = [tuple(start)]
        visited = set()

        def is_wall(x, y):
            return not (0 <= x < n and 0 <= y < m) or maze[x][y] == 1

        while stack:
            xy = stack.pop()
            if xy in visited:
                continue
            visited.add(xy)
            x, y = xy
            if x == dest[0] and y == dest[1]:
                return True
            for dx, dy in dirs:
                nx, ny = x, y
                while not is_wall(nx + dx, ny + dy):
                    nx += dx
                    ny += dy
                stack.append((nx, ny))
        return False
