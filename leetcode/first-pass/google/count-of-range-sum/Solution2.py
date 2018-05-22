from collections import defaultdict


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        soln = set()
        for i in xrange(len(nums)):
            if lower <= nums[i] <= upper:
                soln.add((i, i))
        left_sum = defaultdict(list)
        prev = 0
        for i in xrange(len(nums)):
            left_sum[prev + nums[i]].append(i)
            prev += nums[i]
        for k in xrange(lower, upper + 1):
            for s in left_sum:
                if s == k:
                    for j in left_sum[s]:
                        soln.add((0, j))
                if s - k in left_sum:
                    for max_i in left_sum[s]:
                        for j in left_sum[s - k]:
                            if j + 1 < max_i:
                                soln.add((j + 1, max_i))
        return len(soln)
