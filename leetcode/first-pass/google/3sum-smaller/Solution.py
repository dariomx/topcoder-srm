# for now we will be happy with O(n^2 log(n))

from bisect import bisect_left


class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                x = target - (nums[i] + nums[j])
                k = bisect_left(nums, x, j + 1, n - 1)
                if nums[k] >= x:
                    k -= 1
                if k <= j:
                    continue
                ans += k - j
        return ans

