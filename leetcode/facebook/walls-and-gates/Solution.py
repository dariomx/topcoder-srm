from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        def neighbors(x, y):
            for (i, j) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= i < n and 0 <= j < m and rooms[i][j] > 0:
                    yield (i, j)

        def bfs(start):
            visited = set()
            queue = deque([(start, 0)])
            while queue:
                node, dist = queue.popleft()
                x, y = node
                rooms[x][y] = min(rooms[x][y], dist)
                for nei in neighbors(x, y):
                    i, j = nei
                    if nei not in visited and rooms[i][j] > dist + 1:
                        visited.add(nei)
                        queue.append((nei, dist + 1))

        # main
        n = len(rooms)
        m = len(rooms[0]) if rooms else 0
        if 0 in (n, m):
            return
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    bfs((i, j))
