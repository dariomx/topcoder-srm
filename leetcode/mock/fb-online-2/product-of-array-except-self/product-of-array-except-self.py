class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        post = [1] * n
        post[n - 1] = nums[n - 1]
        for i in reversed(range(n - 1)):
            post[i] *= nums[i] * post[i + 1]
        pre = 1
        ans = []
        for i, x in enumerate(nums):
            prod = pre
            if i + 1 < n:
                prod *= post[i + 1]
            ans.append(prod)
            pre *= x
        return ans
