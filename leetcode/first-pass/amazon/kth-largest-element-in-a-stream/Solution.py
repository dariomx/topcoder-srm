from bisect import insort

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(map(lambda x: -x, nums))[:k]

    def add(self, val):
        insort(self.nums, -val)
        del self.nums[self.k:]
        return -self.nums[-1]