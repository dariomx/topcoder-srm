class Solution(object):
    def increasingTriplet(self, nums):
        if not nums:
            return False
        min_i = 0
        min_j = None
        max_i = 0
        max_j = None
        for k in range(1, len(nums)):
            x = nums[k]
            if (min_j and nums[min_j] < x) or (max_j and nums[max_j] < x):
                return True
            if x > nums[min_i]:
                min_j = k
            else:
                min_i = k
            if x > nums[max_i]:
                max_j = k
            else:
                max_i = k
        return False
