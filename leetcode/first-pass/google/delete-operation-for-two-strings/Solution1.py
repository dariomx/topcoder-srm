"""
This is pretty much same version as my previous solution, but making a little
bit of justince to original intuition: the recursive step can extend to the
right as well (not just to the left, as the solution in Wikipedia).

While this is correct as well (passed once all tests), it turns out to be
slower than extending to the left.
"""


class Solution(object):
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        cache = dict()

        def rec(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if not (0 <= i < n) or not (0 <= j < m):
                ret = 0
            elif word1[i] == word2[j]:
                ret = rec(i + 1, j + 1) + 1
            else:
                ret = max(rec(i, j + 1), rec(i + 1, j))
            cache[(i, j)] = ret
            return ret

        max_len = 0
        for i in xrange(n):
            for j in xrange(m):
                max_len = max(max_len, rec(i, j))
        return (n - max_len) + (m - max_len)
