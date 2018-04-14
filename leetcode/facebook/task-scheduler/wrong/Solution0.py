from heapq import heappush, heappop
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        task_cnt = Counter(tasks)
        cool = []
        for task in task_cnt:
            heappush(cool, (-1, task_cnt[task], task))
        clock = 0
        idle = 0
        while cool:
            last, cnt, task = heappop(cool)
            if last < 0 or clock - last > n:
                print(task)
                if cnt > 1:
                    heappush(cool, (clock, cnt - 1, task))
            else:
                print("idle")
                heappush(cool, (last, cnt, task))
                idle += 1
            clock += 1
        return len(tasks) + idle
