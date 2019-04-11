class Solution(object):
    def anyNodeInCycle(self, head):
        turtle = head
        hare = head
        while turtle:
            turtle = turtle.next
            if hare:
                hare = hare.next
            if hare:
                hare = hare.next
            if turtle == hare:
                return turtle
        return None

    def lenToEnd(self, start, end):
        jumps = 0
        while True:
            jumps += 1
            start = start.next
            if start == end:
                break
        return jumps

    def moveFwd(self, start, k):
        for _ in range(k):
            start = start.next
        return start

    def detectCycle(self, head):
        x = self.anyNodeInCycle(head)
        if x is None:
            return None
        lenCycle = self.lenToEnd(x, x)
        lenX = self.lenToEnd(head, x)
        diff = abs(lenCycle - lenX)
        y = head
        if lenCycle > lenX:
            x = self.moveFwd(x, diff)
        elif lenX > lenCycle:
            y = self.moveFwd(y, diff)
        while x != y:
            x = x.next
            y = y.next
        return x
