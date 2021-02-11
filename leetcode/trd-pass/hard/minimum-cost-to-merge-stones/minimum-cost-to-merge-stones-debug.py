from functools import cache
from math import inf
from typing import List


class CompressArray:
    def __init__(self, A, lo, hi, val):
        self.A = A
        self.lo = lo
        self.hi = hi
        self.size = hi - lo + 1
        self.val = val
        self.hk = self._hashKey()

    def __getitem__(self, i):
        if i < self.lo:
            return self.A[i]
        elif i == self.lo:
            return self.val
        else:
            return self.A[i - self.lo + self.hi]

    def __len__(self):
        if self.lo < inf:
            return len(self.A) - self.size + 1
        else:
            return len(self.A)

    def _hashKey(self):
        mask = (1 << len(self.A)) - 1
        key = mask
        if self.lo < inf:
            for i in range(self.lo, self.hi+1):
                key &= ~(1 << i) & mask
        return key

    def __hash__(self):
        return self.hk


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        ans = self.merge(CompressArray(stones, inf, -inf, 0), K)
        return ans if ans < inf else -1

    @cache
    def merge(self, stones, K: int) -> int:
        n = len(stones)
        if n <= 1:
            return 0
        ans = inf
        cost = 0
        for end in range(n):
            start = end - K + 1
            cost += stones[end]
            if start - 1 >= 0:
                cost -= stones[start - 1]
            if start >= 0 and end - start + 1 >= K:
                recStones = CompressArray(stones, start, end, cost)
                ans = min(ans, cost + self.merge(recStones, K))
        return ans

# main
stones = [69,39,79,78,16,6,36,97,79,27,14,31,4]
K = 2
print(Solution().mergeStones(stones, K))
