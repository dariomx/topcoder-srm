class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        stones_ix = {v: i for (i, v) in enumerate(stones)}
        cache = dict()

        def rec(i, k):
            if (i, k) in cache:
                return cache[i, k]
            if k <= 0:
                ret = False
            elif i == n - 1:
                ret = True
            else:
                ret = False
                for nk in (k, k - 1, k + 1):
                    ni = stones_ix.get(stones[i] + nk, None)
                    if ni is not None and ni > i and rec(ni, nk):
                        ret = True
                        break
            cache[i, k] = ret
            return ret

        return (stones[1] - stones[0]) == 1 and rec(1, 1)


