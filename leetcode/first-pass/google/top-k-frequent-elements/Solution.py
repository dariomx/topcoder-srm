from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums, k):
        cnt = [(-c, x) for (x, c) in Counter(nums).items()]
        heapify(cnt)
        ans = []
        for _ in range(k):
            _, x = heappop(cnt)
            ans.append(x)
        return ans