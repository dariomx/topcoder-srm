# port of @jmracek solution to Python3 (no special handling for negative psum)

from collections import defaultdict


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cnt = defaultdict(lambda: 0)
        cnt[0] = 1
        psum = 0
        ans = 0
        for x in A:
            psum += x
            i = psum % K
            ans += cnt[i]
            cnt[i] += 1
        return ans

