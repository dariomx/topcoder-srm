class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        zerorow = [False] * m
        zerocol = [False] * n
        for i in range(m):
            for j in range(n):
                is_zero = (matrix[i][j] == 0)
                zerorow[i] = zerorow[i] or is_zero
                zerocol[j] = zerocol[j] or is_zero
        for i in range(m):
            for j in range(n):
                if zerorow[i] or zerocol[j]:
                    matrix[i][j] = 0