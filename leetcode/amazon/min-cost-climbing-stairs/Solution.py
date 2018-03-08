"""
Python3 recursive solution with caching.

I was not originally getting right the problem statement, until a friend at
work clarified that one should count until we get "out of" the array; hence,
is not enough to reach the final position, one must "leave" the array as well.

With that clarification in mind I just adjusted my usual recursive approach.
I guess some people might call this a DP solution, given its sub-problem
structure and stuff.

There is an implicit O(n) space cost due recursion, but the time seems to be
O(n) as well, because every index i-th is processed just once (second and
further usages go to the cache).
"""

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

