from sortedcontainers import SortedKeyList

class MaxStack:
    def __init__(self):
        self.by_time = SortedKeyList(key=lambda t: -t[1])
        self.by_val = SortedKeyList(key=lambda t: (-t[0], -t[1]))
        self.time = -1

    def push(self, x: int) -> None:
        self.time += 1
        rec = (x, self.time)
        self.by_time.add(rec)
        self.by_val.add(rec)

    def pop(self) -> int:
        rec = self.by_time.pop(0)
        self.by_val.remove(rec)
        return rec[0]

    def top(self) -> int:
        rec = self.by_time[0]
        return rec[0]

    def peekMax(self) -> int:
        rec = self.by_val[0]
        return rec[0]

    def popMax(self) -> int:
        rec = self.by_val.pop(0)
        self.by_time.remove(rec)
        return rec[0]
