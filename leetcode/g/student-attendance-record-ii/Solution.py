from itertools import permutations as perm


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        pos = set()
        for s in ('', 'A', 'L', 'LL', 'AL', 'ALL'):
            seq = ''.join(s).upper().rjust(n, 'P')
            if len(seq) == n:
                pos |= set(perm(seq))
        print(pos)
        return len(pos)
