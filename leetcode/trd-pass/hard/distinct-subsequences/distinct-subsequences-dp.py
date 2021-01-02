class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][m] = 1
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
                dp[i][j] += dp[i + 1][j]
        return dp[0][0]
