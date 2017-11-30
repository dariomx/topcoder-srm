"""
Each index has a list of candidate numbers which could be put there, so we compute first those lists for all indexes. This quadratic pre-computation can be avoided if we merge with the rest of the logic, but I did not think about that possibility (later I knew, after checking the editorial solution).

Anyway, as I was saying, once we know the list of candidates for each index; we recursively search through the space of ordenations (each index can offer any of its options). We filter such space such that we only keep permutations.

The bulk of work is done at the "rec" function: at each call it receives the remaining candidates for each index, the position i-th where we need to put next candidate, the current permutation and a counter for the # of solutions.

If the index == (n+1), it means we have formed a potencial permutation; but we need to validate that it actually contains all the elements. On the recursive case, we iterate over all candidates for index i-th, adding them into permutation and calling recursively for next index  (i+1)-th. Given that perm argument is shared, we need to "clean" such addition after the recursive call.

We try to optimize to some extent, by pruning some branches:

1) If there are no more candidates for index i-th
2) If we do not have enough elements so far in the permutation
3) If a particular candidate already appears in the so-far formed permutation.

"""

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
