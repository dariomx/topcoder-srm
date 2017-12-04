class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = 0
        curr = 0
        n = len(nums)
        for i in xrange(n):
            if nums[i]:
                curr += 1
            if not nums[i] or i == (n - 1):
                currMax = max(currMax, curr)
                curr = 0
        return currMax
