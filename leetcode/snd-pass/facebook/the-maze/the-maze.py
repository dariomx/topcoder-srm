class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int],
                dest: List[int]) -> bool:
        n, m = len(maze), len(maze[0])
        dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        inv = lambda d: (-d[0], -d[1])
        stack = [(tuple(start), d) for d in dirs]
        visited = set()
        while stack:
            xy, dir = stack.pop()
            nx, ny = xy[0] + dir[0], xy[1] + dir[1]
            if not (0 <= nx < n and 0 <= ny < m) or maze[nx][ny] == 1:
                if (xy[0] == dest[0] and xy[1] == dest[1]):
                    return True
                elif xy not in visited:
                    visited.add(xy)
                    inv_dir = inv(dir)
                    for d in dirs:
                        if d not in (dir, inv_dir):
                            stack.append((xy, d))
            else:
                stack.append(((nx, ny), dir))
        return False
