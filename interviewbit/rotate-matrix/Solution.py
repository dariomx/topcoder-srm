class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        for i in xrange(n):
            for j in xrange(i, i + (n - 2 * i) - 1):
                val = A[i][j]
                x, y = i, j
                while True:
                    A[y][n - 1 - x], val = val, A[y][n - 1 - x]
                    x, y = y, n - 1 - x
                    if (x, y) == (i, j):
                        break
        return A


