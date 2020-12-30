# could not make it and saw editorial; adapted to used sorted list though slower

from sortedcontainers import SortedList


class ExamRoom:
    def __init__(self, N: int):
        self.used = SortedList()
        self.N = N

    def _addSentinel(self):
        if self.used[0] != 0:
            fst = -self.used[0]
            self.used.add(fst)
        else:
            fst = None
        if self.used[-1] != self.N - 1:
            last = self.N - 1 + (self.N - 1 - self.used[-1])
            self.used.add(last)
        else:
            last = None
        return fst, last

    def _removeSentinel(self, sentinel):
        fst, last = sentinel
        if fst:
            self.used.remove(fst)
        if last:
            self.used.remove(last)

    def seat(self) -> int:
        if len(self.used) == 0:
            p = 0
        else:
            sentinel = self._addSentinel()
            p = None
            maxDist = -inf
            for i in range(len(self.used) - 1):
                q = (self.used[i] + self.used[i + 1]) // 2
                minDist = min(q - self.used[i], self.used[i + 1] - q)
                if minDist > maxDist:
                    maxDist = minDist
                    p = q
            self._removeSentinel(sentinel)
        self.used.add(p)
        return p

    def leave(self, p: int) -> None:
        self.used.remove(p)
