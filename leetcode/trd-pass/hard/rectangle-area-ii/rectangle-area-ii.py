# vertical swepping; not my idea, taken from editorial (just adapted
# to do vertical rather than horizontal swapping)

from sortedcontainers import SortedList

OPEN = 1
CLOSE = 2


class Solution:
    def getEvents(self, rects):
        events = defaultdict(list)
        for x1, y1, x2, y2 in rects:
            events[x1].append((OPEN, y1, y2))
            events[x2].append((CLOSE, y1, y2))
        return sorted(events.items(), key=lambda t: t[0])

    def procEvents(self, events, active):
        for typ, y1, y2 in events:
            intv = (y1, y2)
            if typ == OPEN:
                active.add(intv)
            else:
                active.remove(intv)

    def mergeIntervals(self, intvs):
        if not intvs:
            return
        a, b = intvs[0]
        for i in range(1, len(intvs)):
            c, d = intvs[i]
            if a <= c <= b:
                a = min(a, c)
                b = max(b, d)
            else:
                yield (a, b)
                a, b = c, d
        yield (a, b)

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = self.getEvents(rectangles)
        active = SortedList()
        modulus = 10 ** 9 + 7
        ans = 0
        for i in range(len(events) - 1):
            x, x_evs = events[i]
            self.procEvents(x_evs, active)
            width = events[i + 1][0] - x
            for y1, y2 in self.mergeIntervals(active):
                ans += width * (y2 - y1)
                ans %= modulus
        return ans
