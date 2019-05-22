class Solution:
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            bit = ((1 << i) & n) >> i
            ans |= bit << (31 - i)
        return ans