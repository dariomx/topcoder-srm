class Solution(object):
    def __init__(self):
        self.bridges = dict()
        self.bridges[(1, 9)] = 5
        self.bridges[(1, 7)] = 4
        self.bridges[(1, 3)] = 2
        self.bridges[(3, 7)] = 5
        self.bridges[(3, 1)] = 2
        self.bridges[(3, 9)] = 6
        self.bridges[(7, 9)] = 8
        self.bridges[(2, 8)] = 5
        self.bridges[(4, 6)] = 5
        for (x, y), z in self.bridges.items():
            if (y, x) not in self.bridges:
                self.bridges[(y, x)] = z

    def permRec(self, arr, k):
        if k == 1:
            yield list(arr)
        else:
            for i in xrange(k - 1):
                for p in self.permRec(arr, k - 1):
                    yield p
                j = i if k % 2 == 0 else 0
                arr[j], arr[k - 1] = arr[k - 1], arr[j]
            for p in self.permRec(arr, k - 1):
                yield p

    def perm(self, arr):
        for p in self.permRec(arr, len(arr)):
            yield p

    def combRec(self, arr, i, k, curr):
        if len(curr) == k:
            yield list(curr)
        elif i < len(arr):
            for c in self.combRec(arr, i + 1, k, curr):
                yield c
            curr.add(arr[i])
            for c in self.combRec(arr, i + 1, k, curr):
                yield c
            curr.remove(arr[i])

    def comb(self, arr, k):
        for c in self.combRec(arr, 0, k, set()):
            yield c

    def isValidSeq(self, seq):
        used = set()
        used.add(seq[0])
        for i in xrange(len(seq) - 1):
            trans = seq[i], seq[i + 1]
            if trans in self.bridges and \
                            self.bridges[trans] not in used:
                return False
            used.add(seq[i + 1])
        return True

    def allValidSeq(self, arr, m, n):
        for k in xrange(m, n + 1):
            for c in self.comb(arr, k):
                for p in self.perm(c):
                    if self.isValidSeq(p):
                        yield p

    def cntValidSeq(self, arr, m, n):
        cnt = 0
        for k in xrange(m, n + 1):
            for c in self.comb(arr, k):
                for p in self.perm(c):
                    if self.isValidSeq(p):
                        cnt += 1
        return cnt

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        all = set(range(1,10))
        cnt = 4 * self.cntValidSeq(list(all - {1}), m, n)
        cnt += 4 * self.cntValidSeq(list(all - {2}), m, n)
        cnt += self.cntValidSeq(list(all - {5}), m, n)
        return cnt

print(Solution().numberOfPatterns(3, 8))