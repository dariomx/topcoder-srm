class Solution:
    def hammingDistance(self, x, y):
        hd = 0
        get_bit = lambda x, i: (x & (1 << i)) >> i
        for i in range(32):
            hd += get_bit(x, i) ^ get_bit(y, i)
        return hd