# kinda peaked before to soln, so not entirely mine

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int],
                         dest: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        start = tuple(start)
        dest = tuple(dest)
        direc = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        queue = deque([(start, d, 0) for d in direc])
        visited = defaultdict(lambda: inf)
        ans = inf
        while queue:
            (x, y), d, empty = queue.popleft()
            if (x, y) == dest:
                ans = min(ans, empty)
            while 0 <= x + d[0] < n and 0 <= y + d[1] < m and maze[x + d[0]][
                y + d[1]] == 0:
                x += d[0]
                y += d[1]
                empty += 1
            nei = (x, y)
            if empty < visited[nei]:
                visited[nei] = empty
                for ndir in direc:
                    queue.append((nei, ndir, empty))
        return ans if ans < inf else -1
1