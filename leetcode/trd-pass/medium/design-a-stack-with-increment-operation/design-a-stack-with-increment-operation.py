class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.inc = [0] * maxSize
        self.idx = -1

    def push(self, x: int) -> None:
        if self.idx < len(self.stack) - 1:
            self.idx += 1
            self.stack[self.idx] = x

    def pop(self) -> int:
        ret = -1
        if self.idx >= 0:
            ret = self.stack[self.idx] + self.inc[self.idx]
            if self.idx - 1 >= 0:
                self.inc[self.idx - 1] += self.inc[self.idx]
            self.stack[self.idx] = 0
            self.inc[self.idx] = 0
            self.idx -= 1
        return ret

    def increment(self, k: int, val: int) -> None:
        if self.idx >= 0:
            i = min(k-1, self.idx)
            self.inc[i] += val
