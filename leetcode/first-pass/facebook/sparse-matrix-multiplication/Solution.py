class Solution:
    def multiply(self, A, B):
        zero_rows = set()
        zero_cols = set()
        n = len(A)
        k = len(B)
        m = len(B[0])
        for i in range(n):
            zero_rows.add(i)
            for j in range(k):
                if A[i][j] != 0:
                    zero_rows.remove(i)
                    break
        for j in range(m):
            zero_cols.add(j)
            for i in range(k):
                if B[i][j] != 0:
                    zero_cols.remove(j)
                    break
        AB = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i in zero_rows or j in zero_cols:
                    continue
                for l in range(k):
                    AB[i][j] += A[i][l] * B[l][j]
        return AB

