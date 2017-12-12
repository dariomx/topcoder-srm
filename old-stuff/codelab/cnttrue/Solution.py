MOD = 1003
Tr = dict()
Fa = dict()

class Solution:
    def _calcTr(self, op, s, cut, e):
        if op == '|':
            tr = Fa[(s, cut - 1)] * Tr[(cut + 1, e)] + \
                 Tr[(s, cut - 1)] * Fa[(cut + 1, e)] + \
                 Tr[(s, cut - 1)] * Tr[(cut + 1, e)]
        elif op == '^':
            tr = Fa[(s, cut - 1)] * Tr[(cut + 1, e)] + \
                 Tr[(s, cut - 1)] * Fa[(cut + 1, e)]
        else:
            tr = Tr[(s, cut - 1)] * Tr[(cut + 1, e)]
        if (s,e) in Tr:
            print("overlap (%d,%d) with %s %d = %d + %d = %d" % (s,e,op,cut,Tr[(s,e)],tr,Tr[(s,e)]+tr))
        else:
            print("firsttt (%d,%d) with %s %d = %d" % (s, e, op, cut,tr))
        Tr[(s,e)] = Tr.get((s,e), 0) + tr

    def _calcFa(self, op, s, cut, e):
        if op == '|':
            fa = Fa[(s, cut - 1)] * Fa[(cut + 1, e)]
        elif op == '^':
            fa = Fa[(s, cut - 1)] * Fa[(cut + 1, e)] + \
                 Tr[(s, cut - 1)] * Tr[(cut + 1, e)]
        else:
            fa = Fa[(s, cut - 1)] * Tr[(cut + 1, e)] + \
                 Tr[(s, cut - 1)] * Fa[(cut + 1, e)] + \
                 Fa[(s, cut - 1)] * Fa[(cut + 1, e)]
        Fa[(s,e)] = Fa.get((s,e), 0) + fa

    # @param A : string
    # @return an integer
    def cnttrue(self, expr):
        n = len(expr)
        Tr.clear()
        Fa.clear()
        for i in xrange(0, n, 2):
            Tr[(i, i)] = 1 if expr[i]=="T" else 0
            Fa[(i, i)] = 1 - Tr[(i, i)]
        for size in xrange(3, n+1, 2):
            for s in xrange(0, n-size+1, 2):
                for cut in xrange(s+1, s+size-1, 2):
                    e = s + size - 1
                    op = expr[cut]
                    self._calcTr(op, s, cut, e)
                    self._calcFa(op, s, cut, e)
        print(Tr)
        print(Fa)
        return Tr[(0, n - 1)] % MOD

print(Solution().cnttrue("T^T^T^F|F&F^F|T^F^T"))
