from sortedcontainers import SortedList

START = 1
END = 0


class MyCalendarThree:
    def __init__(self):
        self.ranges = SortedList(key=lambda t: (t[0], t[1]))

    def book(self, start: int, end: int) -> int:
        rid = len(self.ranges)
        self.ranges.add((start, START, rid))
        self.ranges.add((end, END, rid))
        k = 0
        overlap = set()
        for _, typ, rid in self.ranges:
            if typ == START:
                overlap.add(rid)
            else:
                overlap.remove(rid)
            k = max(k, len(overlap))
        return k
