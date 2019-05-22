class Solution:
    def transpose(self, A):
        n, m = len(A), len(A[0])
        tA = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                tA[j][i] = A[i][j]
        return tA