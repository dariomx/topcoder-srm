class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = nums[0]
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i]
        prod = nums[n - 1]
        ans[n - 1] = ans[n - 2]
        for i in reversed(range(1, n - 1)):
            ans[i] = ans[i - 1] * prod
            prod *= nums[i]
        ans[0] = prod
        return ans
