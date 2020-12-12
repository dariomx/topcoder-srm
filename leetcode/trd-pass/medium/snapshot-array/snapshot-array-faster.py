class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = -1
        self.set_ops = [None] * length
        for i in range(length):
            self.set_ops[i] = [[self.snap_id, 0]]

    def set(self, index: int, val: int) -> None:
        sl = self.set_ops[index]
        if sl[-1][0] < self.snap_id:
            sl.append([self.snap_id, val])
        else:
            sl[-1][1] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        sl = self.set_ops[index]
        start, end = 0, len(sl) - 1
        val = sl[0][1]
        while start <= end:
            mid = (start + end) // 2
            if sl[mid][0] < snap_id:
                val = sl[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return val
