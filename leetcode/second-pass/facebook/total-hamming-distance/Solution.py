class Solution:
    def totalHammingDistance(self, nums):
        n = len(nums)
        k = 30
        ones = [0] * k
        zeros = [0] * k
        for i in range(k):
            for x in nums:
                bit = ((1 << i) & x) >> i
                ones[i] += bit
                zeros[i] += 1 - bit
        tot_dist = 0
        for i in range(k):
            tot_dist += ones[i] * zeros[i]
        return tot_dist
