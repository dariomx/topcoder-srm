from math import inf

class Solution:
    def maxProduct(self, nums: 'List[int]') -> 'int':
        def rec(i, prod):
            nonlocal ans
            ans = max(ans, prod)
            if (i, prod) in cache or i == len(nums):
                return
            else:
                rec(i+1, prod * nums[i])
                rec(i+1, nums[i])
                cache.add((i, prod))
        cache = set()
        ans = nums[0]
        rec(1, nums[0])
        return ans