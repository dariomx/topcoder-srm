class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        @cache
        def rec(i, j):
            if i <= n and j == m:
                return 1
            elif i < n and j < m:
                ret = 0
                if s[i] == t[j]:
                    ret += rec(i + 1, j + 1)
                ret += rec(i + 1, j)
                return ret
            else:
                return 0

        return rec(0, 0)
