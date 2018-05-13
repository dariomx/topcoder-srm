class Solution(object):
    def findMaxLength(self, nums):
        diff = dict()
        zeros = 0
        ones = 0
        max_len = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1
            d = zeros - ones
            if d == 0:
                max_len = max(max_len, j + 1)
            elif d in diff:
                i = diff[d]
                max_len = max(max_len, j - i)
            else:
                diff[d] = j
        return max_len
