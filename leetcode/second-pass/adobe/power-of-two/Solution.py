class Solution:
    def isPowerOfTwo(self, n):
        ones = 0
        while n > 0:
            ones += n & 1
            n >>= 1
        return ones == 1
