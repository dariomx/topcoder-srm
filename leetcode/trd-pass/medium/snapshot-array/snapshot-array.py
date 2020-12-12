from sortedcontainers import SortedList


class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = -1
        self.set_ops = [None] * length
        for i in range(length):
            self.set_ops[i] = SortedList([self.snap_id])
        self.vals = [{self.snap_id: 0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        sl = self.set_ops[index]
        if sl[-1] < self.snap_id:
            sl.add(self.snap_id)
        self.vals[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        sl = self.set_ops[index]
        snap_id = next(
            sl.irange(maximum=snap_id, inclusive=(True, False), reverse=True))
        return self.vals[index][snap_id]

