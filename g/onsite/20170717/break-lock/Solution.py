from datetime import datetime

class Solution:
    def extendSeq(self, seq, comb):
        n = len(comb)
        last = seq[-n:]
        for i in xrange(1, n+1):
            if last[i:] == comb[:-i]:
                return seq[:-n] + last[:i] + comb
        raise ValueError("unable to extend seq")

    def searchNext(self, comb, i, tried):
        prefix = comb[i:]
        maxPostfix = int(''.join(['9'] * i))
        for k in xrange(maxPostfix + 1):
            next = prefix + str(k).zfill(i)
            if next not in tried:
                return next
        return None

    def breakLock(self, n):
        tried = set()
        comb = ''.join(['0'] * n)
        tried.add(comb)
        seq = comb
        while True:
            for i in xrange(1, n+1):
                next = self.searchNext(comb, i, tried)
                if next is not None:
                    break
            if next is None:
                break
            else:
                comb = next
                tried.add(comb)
                seq = self.extendSeq(seq, comb)
        return seq, tried

start = datetime.now()
seq, tried = Solution().breakLock(4)
end = datetime.now()
print(end - start)
print(len(seq))
print(len(tried))
for c in xrange(9999):
    if str(c).zfill(4) not in tried:
        raise ValueError("did not find %s" % c)