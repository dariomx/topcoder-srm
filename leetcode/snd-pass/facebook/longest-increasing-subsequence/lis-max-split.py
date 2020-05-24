"""
in the end this approach did not work out, cause the LIS is not necessarily
build out of LIS of left and right sides respect to maximum index. Some times,
the global LIS needs sub-optimal solutions on each side.
"""

from typing import List

from rmq import RMQ


class Solution:
    def findLIS(self, nums, start, end):
        if start > end:
            return -1, -1, -1
        elif start == end:
            return 1, start, end
        else:
            max_ix = self.rmq.find_max(start, end)
            lis_left, start_left, end_left = \
                self.findLIS(nums, start, max_ix - 1)
            lis_right, start_right, end_right = \
                self.findLIS(nums, max_ix + 1, end)
            if end_left >= 0 and end_right >= 0 and \
                    nums[end_left] < nums[start_right]:
                max_merge = lis_left + lis_right
            else:
                max_merge = 0
            if lis_left + 1 >= max(max_merge, lis_right):
                return lis_left + 1, start_left, max_ix
            elif max_merge >= max(lis_left + 1, lis_right):
                return max_merge, start_left, end_right
            else:
                return lis_right, start_right, end_right

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        self.rmq = RMQ(nums)
        return self.findLIS(nums, 0, n - 1)[0]

# main
A = [3,5,6,2,5,4,19,5,6,7,12]
lis = Solution()
print(lis.lengthOfLIS(A))