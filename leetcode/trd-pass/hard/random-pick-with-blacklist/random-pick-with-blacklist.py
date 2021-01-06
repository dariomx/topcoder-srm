from random import randint


class Solution:
    def __init__(self, N: int, B: List[int]):
        idx = []
        M = len(B) + 1
        offset = [0] * (2 * M)
        start = [0] * (2 * M)
        prev = 0
        size = 0
        for x in [-1] + sorted(B) + [N]:
            s = prev + 1
            e = x - 1
            if s <= e:
                offset[len(idx)] = size
                start[len(idx)] = s
                idx.append(size)
                offset[len(idx)] = size
                start[len(idx)] = s
                size += e - s + 1
                idx.append(size - 1)
            prev = x
        self.idx = idx
        self.offset = offset
        self.start = start
        self.size = size

    def pick(self) -> int:
        x = randint(0, self.size - 1)
        i = bisect_left(self.idx, x)
        return x - self.offset[i] + self.start[i]
