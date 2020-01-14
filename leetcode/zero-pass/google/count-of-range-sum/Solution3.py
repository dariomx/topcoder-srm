from collections import defaultdict


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        cnt = 0
        for i in xrange(len(nums)):
            if lower <= nums[i] <= upper:
                cnt += 1
        left_sum = defaultdict(list)
        prev = 0
        for i in xrange(len(nums)):
            left_sum[prev + nums[i]].append(i)
            prev += nums[i]
        for k in xrange(lower, upper + 1):
            for s in left_sum:
                if s == k:
                    for j in left_sum[s]:
                        if j > 0:
                            cnt += 1
                if s - k in left_sum:
                    for max_i in left_sum[s]:
                        for j in left_sum[s - k]:
                            if j + 1 < max_i:
                                cnt += 1
        return cnt
