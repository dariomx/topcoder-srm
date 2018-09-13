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
        for i in range(n):
            x = nums[i]
            left = max(0, i-k)
            if i-1-left > 0 and abs(x - get_min(left, i-1)) <= t:
                return True
            right = min(n-1, i+k)
            if right-(i+1) > 0 and abs(x - get_max(i+1, right)) <= t:
                return True
        return False