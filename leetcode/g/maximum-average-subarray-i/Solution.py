class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sumk = 0
        n = len(nums)
        for i in xrange(min(n, k)):
            sumk += nums[i]
        mavg = sumk / float(min(n, k))
        for i in xrange(k, n):
            sumk += nums[i]
            if i >= k:
                sumk -= nums[i - k]
            mavg = max(mavg, sumk / float(k))
        return mavg

