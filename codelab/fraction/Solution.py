from math import copysign

class Solution:
    def arr2str(self, arr):
        return "".join(map(str, arr))

    def hasCycle(self, seq, start):
        n = len(seq) - start
        if n == 0:
            return False
        elif n % 2 == 1:
            return False
        else:
            for i in xrange(start, start + n / 2):
                if seq[i] != seq[n / 2 + i]:
                    return False
            return True

    def searchCycle(self, seq):
        m = len(seq)
        start = 0
        while start < m and seq[start] == 0:
            start += 1
        for i in xrange(start, m):
            if self.hasCycle(seq, i):
                return i, seq[i:m]
        return -1, None

    def getDecPart(self, p, q):
        lenQ = len(str(q))
        cycleIter = 2**lenQ
        num = int(str(p) + "0")
        rem = 1
        seq = []
        cycle = None
        iter = 0
        while rem > 0 and cycle is None:
            seq.append(num / q)
            rem = num % q
            num = int(str(rem) + "0")
            iter += 1
            if iter >= cycleIter:
                startCycle, cycle = self.searchCycle(seq)
        if rem == 0:
            return self.arr2str(seq)
        else:
            return self.arr2str(seq[:startCycle]) + \
                   "(" + self.arr2str(cycle) + ")"

    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, p, q):
        signP = copysign(1, p)
        signQ = copysign(1, q)
        p = abs(p)
        q = abs(q)
        ret = str(p / q)
        p = p % q
        if p > 0:
            ret += "." + self.getDecPart(p, q)
        sign = "-" if signP*signQ < 0 else ""
        return sign + ret


print(Solution().fractionToDecimal(87, 22))