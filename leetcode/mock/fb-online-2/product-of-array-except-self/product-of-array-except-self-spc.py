class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        ans[n - 1] = nums[n - 1]
        for i in reversed(range(n - 1)):
            ans[i] *= nums[i] * ans[i + 1]
        pre = 1
        for i, x in enumerate(nums):
            prod = pre
            if i + 1 < n:
                prod *= ans[i + 1]
            ans[i] = prod
            pre *= x
        return ans
