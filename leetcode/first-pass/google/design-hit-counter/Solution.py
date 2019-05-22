from collections import deque


class HitCounter:
    def __init__(self):
        self.win = deque()
        self.cnt = 0

    def hit(self, ts):
        self.cnt += 1
        if not self.win or ts > self.win[-1][0]:
            self.win.append([ts, 1])
        else:
            self.win[-1][1] += 1
        self.adjust(self.win[-1][0])

    def getHits(self, ts):
        self.adjust(ts)
        return self.cnt

    def adjust(self, ts):
        while self.win and ts - self.win[0][0] + 1 > 300:
            self.cnt -= self.win.popleft()[1]
