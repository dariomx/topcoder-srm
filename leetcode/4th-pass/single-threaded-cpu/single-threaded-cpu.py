from collections import deque
from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        itasks = [(e, d, i) for (i, (e, d)) in enumerate(tasks)]
        itasks.sort(key=lambda t: t[0])
        queue = deque(itasks)
        heap = []
        t = queue[0][0]
        ans = []

        while queue or heap:
            while queue and queue[0][0] <= t:
                _, dur, i = queue.popleft()
                heappush(heap, (dur, i))
            if not heap:
                t = queue[0][0]
                continue
            dur, i = heappop(heap)
            ans.append(i)
            t += dur

        return ans
        
