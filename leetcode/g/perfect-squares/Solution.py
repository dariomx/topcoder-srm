from math import sqrt
from sys import maxint

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        coins = [x for x in xrange(1, n + 1) if int(sqrt(x)) ** 2 == x]
        rec = [maxint] * (n + 1)
        rec[0] = 0
        for c in coins:
            rec[c] = 1
        for k in xrange(1, n + 1):
            rec[k] = min([rec[k - c] for c in coins if k - c >= 0]) + 1
        return rec[n]
