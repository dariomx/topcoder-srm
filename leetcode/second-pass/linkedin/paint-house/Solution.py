from sys import maxsize as maxint


class Solution:
    def minCost(self, costs):
        n = len(costs)
        if n == 0:
            return 0
        m = len(costs[0])
        cache = dict()

        def rec(col, i):
            key = (col, i)
            if key in cache:
                return cache[key]
            elif i == n:
                return 0
            else:
                ret = maxint
                for c in range(m):
                    if c != col:
                        ret = min(ret, costs[i][c] + rec(c, i + 1))
                cache[key] = ret
                return ret

        return min(map(lambda c: rec(c, 0), range(m)))
