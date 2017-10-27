from collections import deque

INF = 2147483647


class Solution(object):
    def search_bfs(self, rooms, start):
        queue = deque()
        m, n = len(rooms), len(rooms[0])
        queue.append((start, 0))
        visited = set()
        visited.add(start)
        while queue:
            (x, y), d = queue.popleft()
            if rooms[x][y] == 0:
                return d
            elif rooms[x][y] == INF or rooms[x][y] > 0:
                for i, j in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
                    if 0 <= i < m and 0 <= j < n and \
                                    (i, j) not in visited and rooms[i][j] != -1:
                        visited.add((i, j))
                        queue.append(((i, j), d + 1))
        return INF

    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), 0
        if m > 0:
            n = len(rooms[0])
        if 0 in (m, n):
            return
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == INF:
                    rooms[i][j] = self.search_bfs(rooms, (i, j))
