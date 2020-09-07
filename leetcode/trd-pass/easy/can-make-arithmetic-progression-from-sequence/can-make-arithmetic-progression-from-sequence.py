"""
May not be that clear nor easy to understand, but here it is:

Three passes:

1) Compute candidate difference (diff) and discard all-equal case
2) Compute how many jumps (as factors of diff) each elem is from first one,
   here we can discard jumps which are not factors of diff or are too big.
3) Ensure that the jumps form the canonical arith progression (0, 1, ..., n)
"""


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # fst pass
        fst, snd, last = inf, inf, -inf
        for x in arr:
            if x < fst:
                snd = fst
                fst = x
            elif x < snd:
                snd = x
            last = max(last, x)
        min_diff = snd - fst
        if min_diff == 0:
            return fst == last
            # snd pass
        n = len(arr)
        cnt = [0] * n
        for i in range(n):
            diff = abs(arr[i] - fst)
            jump, r = divmod(diff, min_diff)
            if r == 0 and jump < n:
                cnt[jump] += 1
            else:
                return False
        # trd pass
        for jump in range(n):
            if cnt[jump] != 1:
                return False
        return True

