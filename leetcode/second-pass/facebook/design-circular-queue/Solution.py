class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.buff = [None] * k
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.front is None:
                self.rear = self.front = 0
            else:
                self.rear = (self.rear + 1) % self.k
            self.buff[self.rear] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.front == self.rear:
                self.rear = self.front = None
            else:
                self.front = (self.front + 1) % self.k
            self.size -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.buff[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.buff[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
