class Solution:
    def totalHammingDistance(self, nums):
        n = len(nums)
        total = 0
        for i in range(32):
            ones, zeros = 0, 0
            for x in nums:
                bit = (x & (1 << i)) >> i
                ones += bit
                zeros += 1 - bit
            total += ones * zeros
        return total
