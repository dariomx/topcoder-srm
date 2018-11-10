from collections import deque


class MyStack:
    def __init__(self):
        self.rev = deque()
        self.tmp = deque()

    def push(self, x):
        self.rev.appendleft(x)

    def pop(self):
        self.tmp.clear()
        last = None
        while self.rev:
            last = self.rev.pop()
            if self.rev:
                self.tmp.appendleft(last)
        self.rev, self.tmp = self.tmp, self.rev
        return last

    def top(self):
        last = self.pop()
        self.rev.appendleft(last)
        return last

    def empty(self):
        return not self.rev
