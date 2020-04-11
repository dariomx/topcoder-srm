class MinStack:
    def __init__(self):
        self.stack = []
        self.pmin = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.pmin:
            self.pmin.append(min(self.pmin[-1], x))
        else:
            self.pmin.append(x)

    def pop(self) -> None:
        self.pmin.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pmin[-1]
