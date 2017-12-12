class Solution(object):
    def neighbors(self, matrix, i, j):
        n, m = len(matrix), len(matrix[0])
        for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < n and 0 <= y < m:
                yield (x, y)

    def is_start(self, matrix, i, j):
        for (x, y) in self.neighbors(matrix, i, j):
            if matrix[x][y] < matrix[i][j]:
                return False
        return True

    def sorted_gt_neighbors(self, matrix, i, j):
        gt = lambda (x, y): matrix[x][y] > matrix[i][j]
        gt_neighbors = filter(gt, self.neighbors(matrix, i, j))
        val = lambda (i, j): matrix[i][j]
        return sorted(gt_neighbors, key=val)

    def search(self, matrix, start, cache):
        if start in cache:
            return cache[start]
        i, j = start
        max_len = 0
        for (x, y) in self.sorted_gt_neighbors(matrix, i, j):
            max_len = max(max_len, self.search(matrix, (x, y), cache))
        max_len += 1
        cache[start] = max_len
        return max_len

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n, m = len(matrix), 0
        if n > 0:
            m = len(matrix[0])
        if 0 in (n, m):
            return 0
        max_len = 0
        cache = dict()
        for i in xrange(n):
            for j in xrange(m):
                if self.is_start(matrix, i, j):
                    max_len = max(max_len, self.search(matrix, (i, j), cache))
        return max_len
