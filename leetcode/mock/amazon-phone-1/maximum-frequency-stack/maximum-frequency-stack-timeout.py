from collections import defaultdict
from heapq import heappush, heappop


class FreqStack:
    def __init__(self):
        self.cnt = dict()
        self.max_cnt = 0
        self.clock = 0
        self.vals = defaultdict(dict)

    def push(self, x: int) -> None:
        old_cnt = self.cnt.get(x, 0)
        new_cnt = old_cnt + 1
        self.cnt[x] = new_cnt
        times = self.vals[old_cnt].pop(x, [])
        heappush(times, -self.clock)
        self.clock += 1
        self.vals[new_cnt][x] = times
        if new_cnt > self.max_cnt:
            self.max_cnt = new_cnt

    def pop(self) -> int:
        cand = self.vals[self.max_cnt]
        max_time = -1
        latest = None
        for x, times in cand.items():
            if -times[0] > max_time:
                max_time = -times[0]
                latest = x
        self.cnt[latest] -= 1
        if self.cnt[latest] == 0:
            self.cnt.pop(latest)
        times = cand.pop(latest)
        heappop(times)
        if len(times) > 0:
            self.vals[self.max_cnt - 1][latest] = times
        if len(cand) == 0:
            self.vals.pop(self.max_cnt)
        self.max_cnt = max(self.vals.keys())
        return latest

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()