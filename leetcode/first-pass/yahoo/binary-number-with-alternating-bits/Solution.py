class Solution:
    def get_mask(self, n):
        mask = 0
        while n != 0:
            mask = (mask << 1) | 1
            n >>= 1
        return mask >> 1

    def hasAlternatingBits(self, n):
        mask = self.get_mask(n)
        return ~((n >> 1) ^ (n & mask)) & mask == 0