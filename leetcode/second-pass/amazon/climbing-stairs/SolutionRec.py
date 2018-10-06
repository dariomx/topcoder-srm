class Solution:
    def climbStairs(self, n):
        cache = dict()

        def rec(m):
            if m in cache:
                return cache[m]
            if m <= 1:
                ret = 1
            else:
                ret = rec(m - 1) + rec(m - 2)
            cache[m] = ret
            return ret

        return rec(n)

