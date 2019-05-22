class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            n = len(A[i])
            for j in range(n // 2 + n % 2):
                A[i][j], A[i][n - 1 - j] = 1 - A[i][n - 1 - j], 1 - A[i][j]
        return A
