from sys import maxint


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        sump = [0] * n
        sump[0] = nums[0]
        for i in xrange(1, n):
            sump[i] = sump[i - 1] + nums[i]
        max_avg = -maxint
        for i in xrange(n):
            for j in xrange(i, n):
                m = j - i + 1
                if m >= k:
                    sum_sub = sump[j] - sump[i] + nums[i]
                    avg = sum_sub / float(m)
                    max_avg = max(max_avg, avg)
        return max_avg
