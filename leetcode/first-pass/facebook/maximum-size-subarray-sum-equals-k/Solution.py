class Solution:
    def maxSubArrayLen(self, nums, k):
        n = len(nums)
        psum = [0] * n
        cache = {0:-1}
        max_size = 0
        for end in range(n):
            psum[end] = nums[end]
            if end-1 >= 0:
                psum[end] += psum[end-1]
            key = psum[end] - k
            if key in cache:
                start = cache[key]
                max_size = max(max_size, end - start)
            if psum[end] not in cache:
                cache[psum[end]] = end
        return max_size 