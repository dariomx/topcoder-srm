from math import inf
from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = -inf
        n = len(heaters)
        for pos in houses:
            i = min(len(heaters)-1, bisect_left(heaters, pos))
            if heaters[i] == pos:
                dist = 0
            else:
                dist = min(abs(pos - heaters[i-1]), abs(pos - heaters[i]))
            ans = max(ans, dist)
        return ans