class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        psum = dict()
        prev = 0
        for i in xrange(len(nums)):
            psum[prev + nums[i]] = i
            prev += nums[i]
        soln = set()
        for k in xrange(lower, upper + 1):
            for s in psum:
                if s == k:
                    print((s, k))
                    soln.add((0, psum[s]))
                elif s - k in psum:
                    min_i = min(psum[s], psum[s - k])
                    max_i = max(psum[s], psum[s - k])
                    if min_i < max_i:
                        soln.add((min_i, max_i))
        print(psum)
        print(soln)
        return len(soln)
