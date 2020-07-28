from collections import defaultdict
from heapq import heappush, heappop


class FreqStack:
    def __init__(self):
        self.pqueue = []
        self.entries = dict()
        self.cnt = defaultdict(lambda: 0)
        self.time = defaultdict(list)
        self.clock = 0

    def push(self, x: int) -> None:
        self.cnt[x] += 1
        self.time[x].append(self.clock)
        self.clock += 1
        self._update_entry(x)

    def pop(self) -> int:
        while self.pqueue:
            _, deleted, x = heappop(self.pqueue)
            if deleted:
                continue
            self.cnt[x] -= 1
            self.time[x].pop()
            self._update_entry(x)
            return x
        raise ValueError('could not pop properly')

    def _update_entry(self, x):
        if x in self.entries:
            self.entries[x][1] = True
        if self.cnt[x] > 0:
            entry = [(-self.cnt[x], -self.time[x][-1]), False, x]
            self.entries[x] = entry
            heappush(self.pqueue, entry)
