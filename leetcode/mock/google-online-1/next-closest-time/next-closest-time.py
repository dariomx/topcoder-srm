class Solution:
    def nextTime(self, h, m):
        m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        return h, m

    def timeDigits(self, h, m):
        return {h // 10, h % 10, m // 10, m % 10}

    def nextClosestTime(self, time: str) -> str:
        h, m = map(int, time.split(':'))
        digits = self.timeDigits(h, m)
        h, m = self.nextTime(h, m)
        while len(self.timeDigits(h, m) - digits) > 0:
            print(h, m)
            h, m = self.nextTime(h, m)
        return "%02d:%02d" % (h, m)