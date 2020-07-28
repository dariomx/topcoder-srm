class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n + 1)]
        for i in range(n):
            dp[1][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[2][i] = True
        for k in range(3, n + 1):
            for i in range(n - k + 1):
                dp[k][i] = i + 1 < n and dp[k - 2][i + 1] and i + k - 1 < n \
                           and \
                           s[i] == s[i + k - 1]
        for k in reversed(range(1, n + 1)):
            for i in range(n):
                if dp[k][i]:
                    return s[i:i + k]
        return ''


