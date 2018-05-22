class Solution(object):
    def minCostClimbingStairs(self, cost):
        cache = dict()
        def rec(cost, i):
            if i in cache:
                return cache[i]
            if not cost or i >= len(cost):
                ret = 0
            else:
                cost1 = rec(cost, i+1)
                cost2 = rec(cost, i+2)
                ret = cost[i] + min(cost1, cost2)
            cache[i] = ret
            return ret
        return min(rec(cost, 0), rec(cost, 1))

