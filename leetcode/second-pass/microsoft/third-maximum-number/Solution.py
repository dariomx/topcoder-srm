from bisect import bisect_left
from math import inf


class Solution:
    def thirdMax(self, nums):
        k = 3
        maxn = [inf] * k
        for x in nums:
            x = -x
            i = bisect_left(maxn, x)
            if i < k and maxn[i] != x:
                maxn.insert(i, x)
                if len(maxn) > k:
                    maxn.pop()
        return -(maxn[0] if maxn[-1] == inf else maxn[-1])
