import sys

MAX_INT = sys.maxint

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, str, k):
        str = str.strip()
        n = len(str)
        rec = [[MAX_INT for _ in xrange(k)] for _ in xrange(n)]
        cntB, cntW = [0]*n, [0]*n
        #
        B = lambda idx: 1 if str[idx] == "B" else 0
        W = lambda idx: 1 if str[idx] == "W" else 0
        #
        def initDiag():
            for i in xrange(k):
                rec[i][i] = 0
        #
        def initFstCol():
            for i in xrange(0, n):
                cntB[i], cntW[i] = cntB[i-1] + B(i), cntW[i-1] + W(i)
                rec[i][0] = cntB[i] * cntW[i]
        # main
        if n < k:
            return -1
        initDiag()
        initFstCol()
        for j in xrange(1, k):
            for i in xrange(j+1, n):
                hCntB, hCntW = cntB[i], cntW[i]
                for h in xrange(0, i):
                    hCntB, hCntW = hCntB - B(h), hCntW - W(h)
                    rec[i][j] = min(rec[i][j], rec[h][j-1] + hCntB*hCntW)
        return rec[n-1][k-1] if rec[n-1][k-1]>=0 else -1
