from math import ceil

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def avgset(self, A):
        def addPrevSoln(A, n, s, prev, rec, i, k):
            m = ceil(n / float(s) * k)
            rec[k] += [x for x in prev[k] if len(x) <= m]
            #for x in prev[k]:
            #    if len(x) <= m:
            #        rec[k].append(x)
            if A[i] == k:
                rec[k].append([i])
            if (k - A[i]) >= 0 and prev[k - A[i]]:
                for x in prev[k - A[i]]:
                    newSoln = x + [i]
                    if len(x) < m and (not rec[k] or rec[k][0] > newSoln):
                        rec[k] = [newSoln]
        #
        def getSubsetSum(A, n, s, kmax):
            prev = [[] for _ in xrange(kmax + 1)]
            rec = prev[:]
            prev[0] = []
            for k in xrange(1, kmax + 1):
                if A[0] == k:
                    prev[k].append([0])
            for i in xrange(1, n):
                for k in xrange(1, kmax + 1):
                    addPrevSoln(A, n, s, prev, rec, i, k)
                prec, rec = rec, prev
                if k < kmax:
                    for k in xrange(kmax+1):
                        rec[k][:] = []
            return rec
        #
        n = len(A)
        A = sorted(A)
        s = sum(A)
        kmax = (s / n) * (n - 1)
        rec = getSubsetSum(A, n, s, kmax)
        getElem = lambda x: map(A.__getitem__, x)
        keySoln = lambda x: (len(x), getElem(x))
        for m in xrange(1, n):
            k = (s / n) * m
            if k/m != (s-k)/(n-m):
                continue
            soln = [x for x in rec[k] if len(x)==m]
            if soln:
                idxFst = min(soln, key=keySoln)
                idxSnd = [i for i in xrange(n) if i not in idxFst]
                idxPair = sorted([idxFst, idxSnd], key=keySoln)
                return map(getElem, idxPair)
        return []

#A = [1, 7, 15, 29, 11, 9]
#A = [ 5, 16, 3, 4, 5, 2, 16, 49, 10, 35, 33, 14, 30, 40, 22, 7, 24, 38, 47, 19, 42 ]
#A = [ 21, 4 ]
#A = [ 19, 5, 38, 22, 44, 12, 17, 35 ]
#A = [ 27, 25, 14, 23, 34, 45, 37, 38, 44, 20, 36, 9, 19, 43, 42, 10, 50, 23 ]

# incorrect answers
# A = [ 18, 29, 0, 47, 0, 41, 40, 28, 7, 1 ]
# mine = [1, 41], [0, 0, 7, 18, 28, 29, 40, 47]
# codelab = []
#
# A = [ 33, 0, 19, 49, 29, 29, 28, 41, 36, 40, 24, 34, 35, 26, 1, 0, 27, 12, 13, 50, 4, 0, 45, 39, 26 ]
# mine: [1, 49], [0, 0, 0, 4, 12, 13, 19, 24, 26, 26, 27, 28, 29, 29, 33, 34, 35, 36, 39, 40, 41, 45, 50])
# codelab: [0 0 29 49 50 ] [0 1 4 12 13 19 24 26 26 27 28 29 33 34 35 36 39 40 41 45 ]


print(Solution().avgset(A))