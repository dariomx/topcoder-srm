from collections import defaultdict


class Solution:
    def multiply(self, A, B):
        n = len(A)
        k = len(A[0])
        m = len(B[0])
        rows_A = defaultdict(lambda: dict())
        for i in range(n):
            for j in range(k):
                if A[i][j] != 0:
                    rows_A[i][j] = A[i][j]
        cols_B = defaultdict(lambda: dict())
        for j in range(m):
            for i in range(k):
                if B[i][j] != 0:
                    cols_B[j][i] = B[i][j]
        mult_AB = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for x in rows_A[i].keys() & cols_B[j].keys():
                    mult_AB[i][j] += rows_A[i][x] * cols_B[j][x]
        return mult_AB

