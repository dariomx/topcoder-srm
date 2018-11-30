from math import inf

class Solution:
    def smallestRangeI(self, A, K):
        D = max(A) - min(A)
        closest = inf
        for x in range(-K, K+1):
            for y in range(-K, K+1):
                dist = D - (x + y)
                if dist >= 0:
                    closest = min(closest, dist)
                    if closest == 0:
                        return 0
        return closest