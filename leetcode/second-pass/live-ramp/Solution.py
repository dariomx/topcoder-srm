from heapq import heapify, heappop


class Solution:
    def findUnsortedSubarray(self, nums):
        incr = list(nums)
        heapify(incr)
        start = 0
        while incr and nums[start] == incr[0]:
            heappop(incr)
            start += 1
        decr = list((-x for x in nums))
        heapify(decr)
        end = len(nums) - 1
        while start < end and decr and nums[end] == -decr[0]:
            heappop(decr)
            end -= 1
        return end - start + 1

