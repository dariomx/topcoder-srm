class Solution:
    def newInteger(self, n: int) -> int:
        base = 9
        pow10 = 1
        ans = 0
        while n >= base:
            n, r = divmod(n, base)
            ans += pow10 * r
            pow10 *= 10
        if n > 0:
            ans += pow10 * n
        return ans
