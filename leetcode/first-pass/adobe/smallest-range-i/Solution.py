from math import inf

class Solution:
    def smallestRangeI(self, A, K):
        D = max(A) - min(A)
        closest = inf
        for x in range(-K, K+1):
            target = D - x
            start, end = -K, K
            while start <= end:
                y = (start + end) // 2
                if target == y:
                    return 0
                elif target < y:
                    end = y - 1
                else:
                    start = y + 1
            closest = min(closest, D - (x+y))
        return closest