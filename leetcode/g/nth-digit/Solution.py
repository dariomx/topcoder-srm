class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        for x in xrange(1, 2 ** 31):
            k = len(str(x))
            if i + k < n:
                i += k
            else:
                for c in str(x):
                    i += 1
                    if i == n:
                        return int(c)
