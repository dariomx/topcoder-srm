from collections import deque


class Solution:
    def bfs(self, queue, rooms):
        m, n = len(rooms), len(rooms[0])
        visited = set()
        while queue:
            (x, y), d = queue.popleft()
            if rooms[x][y] > 0:
                rooms[x][y] = min(rooms[x][y], d)
            for (i, j) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                if rooms[i][j] <= 0 or (i, j) in visited:
                    continue
                visited.add((i, j))
                queue.append(((i, j), d + 1))

    def wallsAndGates(self, rooms):
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        if n == 0:
            return
        queue = deque()
        for x in range(m):
            for y in range(n):
                if rooms[x][y] == 0:
                    queue.append(((x, y), 0))
        self.bfs(queue, rooms)
