from math import factorial as fact


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 3
        elif n == 2:
            return 8
        elif n == 3:
            return 19
        else:
            cnt = 0
            for k in xrange(n / 3 + 1):
                cnt += fact(n - 2 * k + 1)
            return cnt
