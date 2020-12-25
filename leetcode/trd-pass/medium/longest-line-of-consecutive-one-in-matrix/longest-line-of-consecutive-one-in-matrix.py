class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        def upd(x, y):
            nonlocal ans
            y = y + 1 if x == 1 else 0
            ans = max(ans, y)
            return y

        n = len(M)
        if n == 0:
            return 0
        else:
            m = len(M[0])
        row = [0] * n
        col = [0] * m
        diag = [0] * (n + m)
        anti = [0] * (n + m)
        ans = 0
        for i in range(n):
            for j in range(m):
                x = M[i][j]
                row[i] = upd(x, row[i])
                col[j] = upd(x, col[j])
                diag[i - j] = upd(x, diag[i - j])
                anti[i + j] = upd(x, anti[i + j])
        return ans
