class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        n = len(nums)
        if n == 0:
            return False
        pmin = [0] * n
        pmax = [0] * n
        pmin[0] = nums[0]
        pmax[0] = nums[0]
        for i in range(1, n):
            pmin[i] = min(pmin[i-1], nums[i])
            pmax[i] = max(pmax[i-1], nums[i])
        get_min = lambda i, j: min(pmin[i], pmin[j])
        get_max = lambda i, j: max(pmax[i], pmax[j])
        def check(x, i, j):
            return abs(x - get_min(i, j)) <= t or \
                   abs(x - get_max(i, j)) <= t
        for i in range(n):
            x = nums[i]
            left = max(0, i-k)
            if i-1-left > 0 and check(x, left, i-1):
                return True
            right = min(n-1, i+k)
            if right-(i+1) > 0 and check(x, i+1, right):
                return True
        return False