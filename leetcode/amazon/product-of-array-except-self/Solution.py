"""
Python3 solution with O(n) time and O(1) space

If we knew what is the product left-to-right, and right-to-left of any
position, we could compute the i-th result as follows:

out[i] = left[i-1] * right[i+1]

So we could perform 3 passes:

1) Compute left
2) Compute right
3) Compute out

But in order to optimize further and reduce space, we could reuse the output
itself to save left; and compute right as we move backwards.

"""

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        out = [0] * n
        out[0] = nums[0]
        for i in range(1, n-1):
            out[i] = out[i-1] * nums[i]
        right = 1
        for i in range(n-1, 0, -1):
            out[i] = out[i-1] * right
            right *= nums[i]
        out[0] = right
        return out