"""
Recursive DP Python3 solution with cache

We use recursion over a substring s[i:j+1], if the extremes are the same we
count two, otherwise we have two options: dropping the left or the right end.
We recurse to compute both, and just take the maximum.

Given the branching we are doing while recursing, we also cache the results
to allow for reusing (think this is called memoization).

One beer to the one who tells me what is the time complexity, I have a
hangover and cannot think properly now.
"""

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

