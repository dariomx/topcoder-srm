from collections import deque
from sys import maxint


class Solution(object):
    def bfs_search(self, matrix, start, min_dist):
        n, m = len(matrix), len(matrix[0])
        queue = deque([(start, 0)])
        visited = set()
        visited.add((None, start))
        while queue:
            (x, y), dist = queue.popleft()
            if matrix[x][y] == 1:
                min_dist[x][y] = min(min_dist[x][y], dist)
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= i < n and 0 <= j < m:
                    edge = ((x,y), (i,j))
                    if edge in visited:
                        continue
                    visited.add(edge)
                    new_dist = matrix[i][j] * (dist + 1)
                    queue.append(((i, j), new_dist))

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

# main
pp = lambda m: '\n'.join(map(lambda r: ' '.join(map(str,r)), m))
mat = [[0,0,0],[1,1,1],[1,1,1]]
print(pp(mat))
print('**********')
print(pp(Solution().updateMatrix(mat)))
