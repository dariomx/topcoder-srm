class MyQueue:
    def __init__(self):
        self.ord = []
        self.rev = []

    def _rev2ord(self):
        if not self.ord:
            while self.rev:
                self.ord.append(self.rev.pop())

    def push(self, x):
        self.rev.append(x)

    def pop(self):
        self._rev2ord()
        return self.ord.pop()

    def peek(self):
        self._rev2ord()
        return self.ord[-1]

    def empty(self):
        return not self.rev and not self.ord
