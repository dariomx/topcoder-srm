from collections import defaultdict
from bisect import bisect_left


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        n = len(times)
        top = [None] * n
        cnt = defaultdict(lambda: 0)
        cnt[0] = 1
        top[0] = persons[0]
        for i in range(1, n):
            j = persons[i]
            cnt[j] += 1
            if cnt[j] >= cnt[top[i - 1]]:
                top[i] = j
            else:
                top[i] = top[i - 1]
        self.top = top
        self.n = n
        self.times = times

    def q(self, t: int) -> int:
        if t < self.times[0]:
            return -1
        if t > self.times[-1]:
            i = self.n - 1
        else:
            i = bisect_left(self.times, t)
            if t < self.times[i]:
                i -= 1
        return self.top[i]
