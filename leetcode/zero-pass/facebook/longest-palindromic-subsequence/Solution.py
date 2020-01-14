class Solution:
    def longestPalindromeSubseq(self, s):
        cache = dict()

        def rec(s, i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i > j:
                ret = 0
            elif i == j:
                ret = 1
            else:
                if s[i] == s[j]:
                    ret = 2 + rec(s, i + 1, j - 1)
                else:
                    ret = max(rec(s, i + 1, j), rec(s, i, j - 1))
            cache[(i, j)] = ret
            return ret

        return rec(s, 0, len(s) - 1)

