from collections import deque
from sys import maxint


class Solution(object):
    def neighbors(self, matrix, node):
        n, m = len(matrix), len(matrix[0])
        x, y = node
        for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= i < n and 0 <= j < m:
                yield (i, j)

    def dfs_search(self, matrix, start, visited, boundary, min_dist):
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            x, y = node
            for neig in self.neighbors(matrix, node):
                i, j = neig
                if matrix[i][j] == 0:
                    min_dist[x][y] = 1
                    boundary.add(node)
                else:
                    stack.append(neig)

    def bfs_search(self, matrix, start, min_dist):
        n, m = len(matrix), len(matrix[0])
        queue = deque([(start, 1)])
        visited = set()
        visited.add(start)
        while queue:
            node, d = queue.popleft()
            x, y = node
            min_dist[x][y] = min(min_dist[x][y], d)
            for neig in self.neighbors(matrix, node):
                i, j = neig
                if matrix[i][j] == 1 and neig not in visited:
                    visited.add(neig)
                    queue.append((neig, d + 1))

    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(matrix), len(matrix[0])
        ival = lambda i, j: maxint if matrix[i][j] == 1 else 0
        min_dist = [[ival(i, j) for j in xrange(m)] for i in xrange(n)]
        visited = set()
        boundary = set()
        for x in xrange(n):
            for y in xrange(m):
                if matrix[x][y] == 1 and (x, y) not in visited:
                    self.dfs_search(matrix, (x, y), visited, boundary, min_dist)
        for start in boundary:
            self.bfs_search(matrix, start, min_dist)
        return min_dist
