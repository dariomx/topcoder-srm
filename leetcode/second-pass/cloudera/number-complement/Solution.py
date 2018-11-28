class Solution:
    def findComplement(self, num):
        ans = 0
        first_one = False
        for i in range(31, -1, -1):
            bit = ((1 << i) & num) >> i
            first_one = first_one or (bit == 1)
            if first_one:
                ans |= (1 - bit) << i
        return ans