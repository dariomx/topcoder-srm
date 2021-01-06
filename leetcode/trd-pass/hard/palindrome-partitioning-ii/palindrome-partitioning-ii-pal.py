class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [inf] * (n + 1)
        dp[n] = 0
        pal = [[False] * n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True
        for i in reversed(range(n)):
            for j in range(i, n):
                pal[i][j] = s[i] == s[j]
                if j - i + 1 > 2:
                    pal[i][j] = pal[i][j] and pal[i + 1][j - 1]
                if pal[i][j]:
                    dp[i] = min(dp[i], int(j < n - 1) + dp[j + 1])
        return dp[0]
