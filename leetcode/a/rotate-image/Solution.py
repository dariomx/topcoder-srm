class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for x in xrange(n):
            for y in xrange(x, n - x - 1):
                i, j = x, y
                prev = matrix[i][j]
                for _ in xrange(4):
                    i, j = j, n - i - 1
                    prev, matrix[i][j] = matrix[i][j], prev
