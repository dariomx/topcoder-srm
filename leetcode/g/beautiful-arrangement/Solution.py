from collections import defaultdict


class Solution(object):
    def rec(self, cand, i, n, perm, soln):
        if i == n + 1:
            if len(perm) == n:
                soln[0] += 1
        elif not cand[i]:
            return
        elif len(perm) == (i - 1):
            for x in cand[i]:
                if x in perm:
                    continue
                perm[x] = i
                self.rec(cand, i + 1, n, perm, soln)
                del perm[x]

    def countArrangement(self, N):
        cand = defaultdict(lambda: set())
        for i in xrange(1, N + 1):
            for x in xrange(1, N + 1):
                if x % i == 0 or i % x == 0:
                    cand[i].add(x)
        perm = dict()
        soln = [0]
        self.rec(cand, 1, N, perm, soln)
        return soln[0]
