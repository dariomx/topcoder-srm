class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        elif 0 in (n, m):
            return s1 + s2 == s3
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = s1[:i] == s3[:i]
        for j in range(1, m + 1):
            dp[0][j] = s2[:j] == s3[:j]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or \
                           (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])
        return dp[n][m]
