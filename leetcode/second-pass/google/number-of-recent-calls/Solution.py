from collections import deque

class RecentCounter:
    def __init__(self):
        self.win = deque()

    def ping(self, t):
        self.win.append(t)
        while self.win and self.win[0] < t - 3000:
            self.win.popleft()
        return len(self.win)
