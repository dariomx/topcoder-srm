"""
At every iteration i-th we keep two quantities:

pfx = sum(nums[:i+1])
min_pfx = min_{j<i} {sum(nums[:j+1])}

For each new prefix sum pfx, we just need to see if substracting the minimum
prefix seen so far gives bigger sum. This is because computing pfx - min_pfx
is essentially computing sum(nums[j+1:i+1]); hence for i-th position we just
check the subarray on the left with biggest possible sum. This implies O(1)
at every position, hence global O(n) in time with O(1) memory (just a few
scalar vars).

"""

from sys import maxsize as maxint


class Solution:
    def maxSubArray(self, nums):
        pfx = 0
        min_pfx = maxint
        max_sum = -maxint
        for x in nums:
            pfx += x
            max_sum = max(max_sum, pfx, pfx - min_pfx)
            min_pfx = min(min_pfx, pfx)
        return max_sum
