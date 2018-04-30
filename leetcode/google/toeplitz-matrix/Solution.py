class Solution:
    def isToeplitzMatrix(self, matrix):
        n, m = len(matrix), len(matrix[0])

        def check_diag(i, j, size):
            x = matrix[i][j]
            for _ in range(1, size):
                i += 1
                j += 1
                if matrix[i][j] != x:
                    return False
            return True

        for size in range(2, n + 1):
            i, j = n - size, 0
            if not check_diag(i, j, min(size, m)):
                return False
        for size in range(2, m):
            i, j = 0, m - size
            x = matrix[i][j]
            if not check_diag(i, j, min(size, n)):
                return False
        return True
