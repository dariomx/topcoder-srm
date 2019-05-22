"""
Python3 solution with O(1) space and O(n) time.

For the inner loop, we can move forward index, put what we saved before and
remember the value we overwrote. Doing it that way will complete one cycle
of proper assignments.

Trick is that above may not always traverse all elements of array, there could
be more than one of those cycles. Hence we enclose in an outer loop to ensure
that after our last cycle, we continue from next starting point (assuming that
we have not processed all elements yet).
"""

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        start = -1
        m = 0
        while m < n:
            start = (start + 1) % n
            i = start
            v = nums[i]
            while True:
                i = (i + k) % n
                nums[i], v = v, nums[i]
                m += 1
                if i == start:
                    break
