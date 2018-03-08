"""
Python3 solution with a single pass and O(n) space

I do not have yet the level to figure out an O(1) space solution, but at
least I focused on achieving a single-pass algorithm.

Using a booleans array (found), which may be faster than dictionary, we can
do a single pass and compute both the duplicate element as well as the total
sum of the elements (minus the repeated occurrence). There is a well known
formula for the sum of the first n numbers, hence we can use it, subtract
the computed sum and then know what is the missing number.
"""

class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        found = [False] * (n+1)
        dup = None
        sum = 0
        for x in nums:
            if found[x]:
                dup = x
            else:
                found[x] = True
                sum += x
        return [dup, n*(n+1)//2 - sum]