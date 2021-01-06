class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [inf] * (n + 1)
        dp[n] = 0
        for i in reversed(range(n)):
            for j in range(i, n):
                t = s[i:(j + 1)]
                if t == t[::-1]:
                    dp[i] = min(dp[i], int(j < n - 1) + dp[j + 1])
        return dp[0]
