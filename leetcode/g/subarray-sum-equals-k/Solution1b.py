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
                if psum[j] - (psum[i-1] if i > 0 else 0) == k:
                    cnt += 1
        return cnt
