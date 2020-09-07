class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        ans = 0
        pow2 = 1
        r = N
        while r > 0:
            q, r = divmod(r, 2)
            ans += pow2 * (1 - r)
            r = q
            pow2 *= 2
        return ans