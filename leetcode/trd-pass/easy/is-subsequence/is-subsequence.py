class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i, j = 0, 0
        while i < n:
            while j < m and s[i] != t[j]:
                j += 1
            if j == m:
                break
            elif s[i] == t[j]:
                i += 1
                j += 1
        return i == n
