from functools import lru_cache

from math import inf


class Solution:
    @lru_cache(None)
    def superEggDrop(self, K: int, N: int) -> int:
        if K == 1 or N <= 1:
            ret = max(1, N)
        else:
            ret = inf
            for i in range(1, N + 1):
                prev = ret
                ret = min(ret, 1 + max(self.superEggDrop(K - 1, i - 1),
                                       self.superEggDrop(K, N - i)))
                if inf > prev > ret:
                    break
        return ret

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(4000)
print(Solution().superEggDrop(4, 10000))
