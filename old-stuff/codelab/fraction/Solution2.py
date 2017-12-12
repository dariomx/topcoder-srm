from math import copysign

class Solution:
    def arr2str(self, arr):
        return "".join(map(str, arr))

    def getDecPart(self, p, q):
        num = int(str(p) + "0")
        pastNum = dict()
        seq = []
        i = 0
        rem = 1
        while rem > 0 and num not in pastNum:
            seq.append(num / q)
            pastNum[num] = i
            rem = num % q
            i += 1
            num = int(str(rem) + "0")
        if rem == 0:
            return self.arr2str(seq)
        else:
            j = pastNum[num]
            return self.arr2str(seq[:j]) + \
                   "(" + self.arr2str(seq[j:]) + ")"

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
        sign = "-" if signP*signQ < 0 and ret != "0" else ""
        return sign + ret

#print(Solution().fractionToDecimal(87, 22))
#print(Solution().fractionToDecimal(0, -1))
print(Solution().fractionToDecimal(945, 103))