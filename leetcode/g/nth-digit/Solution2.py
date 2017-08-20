from math import log10


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        i = 9
        ln = int(log10(n))
        for p in xrange(1, ln):
            i += i * 10 * (p + 1)
        for x in xrange(10 ** ln, 2 ** 31):
            k = len(str(x))
            if i + k < n:
                i += k
            else:
                for c in str(x):
                    i += 1
                    if i == n:
                        return int(c)

