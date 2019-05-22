class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        n = len(nums)
        prod = [0] * n
        prod[0] = nums[0]
        for i in range(1, n):
            prod[i] = prod[i-1] * nums[i]
        get_prod = lambda i,j: (prod[j] // prod[i]) * nums[i]
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if get_prod(i, j) < k:
                    ans += 1
                else:
                    break
        return ans