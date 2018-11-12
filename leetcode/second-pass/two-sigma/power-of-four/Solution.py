class Solution:
    def isPowerOfFour(self, num):
        fst_one = False
        zeros = 0
        ones = 0
        for i in range(32):
            bit = ((1 << i) & num) >> i
            if bit == 1:
                if not fst_one:
                    fst_one = True
                ones += 1
            elif not fst_one:
                zeros += 1
        return ones == 1 and zeros % 2 == 0
