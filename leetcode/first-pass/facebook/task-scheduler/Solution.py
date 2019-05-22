from heapq import heappush, heappop, heapify
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        cnt = [-k for k in Counter(tasks).values()]
        heapify(cnt)
        last = []
        i = 0
        while cnt or last:
            while last and i - last[0][0] - 1 >= n:
                heappush(cnt, last.pop()[1])
            if cnt:
                k = heappop(cnt)
                if k + 1 < 0:
                    last.append((i, k + 1))
            i += 1
        return i
