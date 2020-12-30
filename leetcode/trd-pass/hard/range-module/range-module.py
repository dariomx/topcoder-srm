from sortedcontainers import SortedKeyList


class RangeModule:
    def __init__(self):
        self.ranges = SortedKeyList(key=lambda t: t[0])

    def addRange(self, left: int, right: int) -> None:
        a, b = left, right
        if len(self.ranges) == 0:
            self.ranges.add((a, b))
            return
        i = self.ranges.bisect_key_left(left)
        if i - 1 >= 0:
            if self.ranges[i-1][0] <= a <= self.ranges[i-1][1]:
                i -= 1
            elif i == len(self.ranges):
                self.ranges.add((a, b))
                return
        add = False
        for j in range(i, len(self.ranges)):
            c, d = self.ranges[j]
            if max(a, c) < min(b, d):
                self.ranges.pop(j)
                x, z = min(a, c), max(b, d)
                self.ranges.add((x, z))
                a, b = x, z
                add = True
            else:
                add = True
                break
        if add:
            self.ranges.add((a, b))

    def queryRange(self, left: int, right: int) -> bool:
        a, b = left, right
        i = self.ranges.bisect_key_left(left)
        if i - 1 >= 0:
            if self.ranges[i-1][0] <= a <= self.ranges[i-1][1]:
                i -= 1
            elif i == len(self.ranges):
                return False
        for j in range(i, len(self.ranges)):
            c, d = self.ranges[j]
            x, y = max(a, c), min(b, d)
            if (x, y) == (c, d):
                if b == d:
                    break
                else:
                    a = d
            elif (x, y) == (a, b):
                break
            else:
                return False
        return True

    def removeRange(self, left: int, right: int) -> None:
        a, b = left, right
        i = self.ranges.bisect_key_left(left)
        if i - 1 >= 0:
            if self.ranges[i-1][0] <= a <= self.ranges[i-1][1]:
                i -= 1
            elif i == len(self.ranges):
                return
        add = True
        for j in range(i, len(self.ranges)):
            c, d = self.ranges[j]
            y, w = max(a, c), min(b, d)
            if y < w:
                self.ranges.pop(j)
                x, z = min(a, c), max(b, d)
                if x < y:
                    self.ranges.add((x, y))
                add = True
                a, b = w, z
            else:
                add = False
                break
        if add:
            self.ranges.add((a, b))

rm = RangeModule()
rm.addRange(5,8)
print(rm.queryRange(3, 4))
rm.removeRange(5,6)
rm.removeRange(3,6)
rm.addRange(1,3)
print(rm.queryRange(2, 3))