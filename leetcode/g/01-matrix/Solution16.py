# this is editorial soln

from sys import maxint


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(matrix), len(matrix[0])
        dist = [[0 for _ in xrange(m)] for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == 1:
                    dist[i][j] = maxint
        for i in xrange(n):
            for j in xrange(m):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        for i in xrange(n - 1, -1, -1):
            for j in xrange(m - 1, -1, -1):
                if i + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist
