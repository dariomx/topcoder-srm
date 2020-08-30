from heapq import heapify, heappop
from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maxHeap = [(-x, k) for (x, k) in Counter(nums).items()]
        heapify(maxHeap)
        lt = dict()
        size = len(nums)
        while maxHeap:
            x, k = heappop(maxHeap)
            size -= k
            lt[-x] = size
        return [lt[x] for x in nums]
