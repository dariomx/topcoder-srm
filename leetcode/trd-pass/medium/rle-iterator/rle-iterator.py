class RLEIterator:
    def __init__(self, A: List[int]):
        self.chunk = []
        for i in range(len(A) - 2, -1, -2):
            if i % 2 == 0 and A[i] > 0:
                self.chunk.append([A[i], A[i + 1]])

    def next(self, n: int) -> int:
        while self.chunk and n > self.chunk[-1][0]:
            n -= self.chunk[-1][0]
            self.chunk.pop()
        if self.chunk:
            self.chunk[-1][0] -= n
            ret = self.chunk[-1][1]
            if self.chunk[-1][0] == 0:
                self.chunk.pop()
        else:
            ret = -1
        return ret
