from functools import lru_cache

from math import inf


class Solution:
    @lru_cache(None)
    def superEggDrop(self, K: int, N: int) -> int:
        print(K, N)
        if K == 1 or N <= 1:
            ret = max(1, N)
        else:
            ret = inf
            for i in range(1, N + 1):
                ret = min(ret, 1 + max(self.superEggDrop(K - 1, i - 1),
                                       self.superEggDrop(K, N - i)))
        return ret

print(Solution().superEggDrop(4, 50))
