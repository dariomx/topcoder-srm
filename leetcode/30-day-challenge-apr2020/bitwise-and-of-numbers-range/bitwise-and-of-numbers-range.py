class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = n - m
        mask = 1
        ans = 0
        for i in range(32):
            bit = ((m & mask) >> i) & ((n & mask) >> i)
            if bit == 1 and diff <= mask:
                ans |= 1 << i
            mask <<= 1
            if mask > m:
                break
        return ans
