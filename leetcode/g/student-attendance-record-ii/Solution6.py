from math import factorial


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """

        def comb(a, b):
            if b > a:
                return 1
            else:
                return fact(a) / (fact(b) * fact(a - b))

        def fact(a):
            if a < 0:
                return 1
            else:
                return factorial(a)

        # main
        if n == 1:
            return 3
        elif n == 2:
            return 8
        else:
            bad = 0
            for i in xrange(3, n + 1):
                for j in xrange(2, n + 1):
                    if i + j > n:
                        continue
                    bad += (n - i + 1) * comb(n - i, j) * (3**(n - i - j))
            for i in xrange(3, n + 1):
                bad += (n - i + 1) * (2**(n - i))
            for j in xrange(2, n + 1):
                bad += comb(n, j) * (2**(n - j))
            return 3 ** n - bad
