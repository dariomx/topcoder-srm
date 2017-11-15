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
        cond = lambda x,y: x % y == 0 or y % x == 0
        for i in xrange(n):
            soln = [nums[i]]
            for j in xrange(i+1, n):
                fst = soln[0]
                last = soln[-1]
                y = nums[j]
                if cond(fst, y) and cond(last, y):
                    soln.append(y)
            if len(soln) > len(max_soln):
                max_soln = soln
        return max_soln