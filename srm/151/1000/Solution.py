from math import sqrt

class Gauss:
    def whichSums(self, target):
        ranges = []
        t = int(target)
        getN = lambda m: sqrt(2 * t + (m - 1) * m + 0.25) - 0.5
        m = 1
        while m < t:
            n = getN(m)
            if int(n) == n:
                ranges.append("[%d, %d]" % (m, n))
                m = n
            else:
                m += 1
        return ranges

target = 42
target = 4
target = 17
target = 55
target = "100000000000"
print(Gauss().whichSums(target))