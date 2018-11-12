class NumArray:
    def __init__(self, nums):
        n = len(nums)
        if n == 0:
            return
        psum = [0] * n
        psum[0] = nums[0]
        for i in range(1, n):
            psum[i] = psum[i-1] + nums[i]
        self.psum = psum
        self.nums = nums

    def sumRange(self, i, j):
        if not self.psum:
            return 0
        else:
            return self.psum[j] - self.psum[i] + self.nums[i]
