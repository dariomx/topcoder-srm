class Solution:
    def findMaxLength(self, nums):
        max_len = 0
        cache = {0: -1}
        no, nz = 0, 0
        for j in range(len(nums)):
            no += nums[j]
            nz += 1 - nums[j]
            key = no - nz
            if key in cache:
                i = cache[key]
                max_len = max(max_len, j - i)
            else:
                cache[key] = j
        return max_len
