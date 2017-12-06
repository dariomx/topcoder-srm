"""
My Python solution with prefix sums: it explores all the O(n^2) subarrays,
but evaluates each subarray [i,j] efficiently in O(1) time with the formula
psum[j] - psum[i]. Sadly, this times out due the language chosen.

See the Java and C ports of the same algorithm (on this same directory),
they get both accepted. Interestingly the Java version runs twice as fast as
the C version! I never thought that I would see the say when C was
outperformed by Java ;-?

"""


class Solution(object):
    def calc_psum(self, nums, n):
        psum = [0] * n
        psum[0] = nums[0]
        for i in xrange(1, n):
            psum[i] = psum[i - 1] + nums[i]
        return psum

    def subarraySum(self, nums, k):
        n = len(nums)
        if n == 0:
            return 0
        psum = self.calc_psum(nums, n)
        cnt = 0
        for i in xrange(n):
            for j in xrange(i, n):
                if psum[j] - (psum[i - 1] if i > 0 else 0) == k:
                    cnt += 1
        return cnt
