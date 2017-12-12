class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        max_soln = []
        for i in xrange(n):
            soln = [nums[i]]
            for j in xrange(i + 1, n):
                x = soln[-1]
                y = nums[j]
                if x % y == 0 or y % x == 0:
                    soln.append(y)
            if len(soln) > len(max_soln):
                max_soln = soln
        return max_soln
