from collections import deque
from sys import maxsize


class Solution(object):
    def bfs_search(self, matrix, start, min_dist):
        n, m = len(matrix), len(matrix[0])
        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)
        while queue:
            (x, y), d = queue.popleft()
            if matrix[x][y] == 1:
                min_dist[x][y] = min(min_dist[x][y], d)
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= i < n and 0 <= j < m and (i, j) not in visited:
                    visited.add((i, j))
                    queue.append(((i, j), d + matrix[i][j]))

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(matrix), len(matrix[0])
        min_dist = [[0 for _ in range(m)] for _ in range(n)]
        for x in range(n):
            for y in range(m):
                if matrix[x][y] == 1:
                    min_dist[x][y] = maxsize
        for x in range(n):
            for y in range(m):
                if matrix[x][y] == 0:
                    self.bfs_search(matrix, (x, y), min_dist)
        return min_dist
