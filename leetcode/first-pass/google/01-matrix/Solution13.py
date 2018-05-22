from collections import deque
from sys import maxint


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
                if 0 <= i < n and 0 <= j < m and \
                                matrix[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    queue.append(((i, j), d + matrix[i][j]))

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(matrix), len(matrix[0])
        min_dist = [[0 for _ in xrange(m)] for _ in xrange(n)]
        for x in xrange(n):
            for y in xrange(m):
                if matrix[x][y] == 1:
                    min_dist[x][y] = maxint
        for x in xrange(n):
            for y in xrange(m):
                if matrix[x][y] == 0:
                    self.bfs_search(matrix, (x, y), min_dist)
        return min_dist
