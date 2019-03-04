class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.i = 0
        self.j = 0
        self.v = v

    def next(self) -> int:
        ret = self.v[self.i][self.j]
        self.j += 1
        if self.j == len(self.v[self.i]):
            self.j = 0
            self.i += 1
        return ret

    def hasNext(self) -> bool:
        while self.i < len(self.v) and not self.v[self.i]:
            self.i += 1
        return self.i < len(self.v) and \
               self.v[self.i] and \
               self.j < len(self.v[self.i])
