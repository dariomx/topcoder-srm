class Solution:
    def numWays(self, n, k):
        def rec(i, color, rep):
            key = (i, color, rep)
            if key in cache:
                return cache[key]
            if rep > 1:
                ret = 0
            elif i == n - 1:
                ret = 1
            else:
                ways = 0
                for j in range(k):
                    ways += rec(i + 1, j, (rep + 1) if j == color else 0)
                ret = ways
            cache[key] = ret
            return ret
            # main

        cache = dict()
        if 0 in (n, k):
            return 0
        else:
            return rec(0, 0, 0) * k
