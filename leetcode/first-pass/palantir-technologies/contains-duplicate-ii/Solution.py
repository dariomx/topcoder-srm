class Solution:
    def containsNearbyDuplicate(self, nums, k):
        start = dict()
        for end in range(len(nums)):
            x = nums[end]
            if x in start and end - start[x] <= k:
                return True
            else:
                start[x] = end
        return False
