from itertools import product


class Solution(object):
    def comb(self, n, cache):
        if n == 0:
            return set([''])
        else:
            if n in cache:
                return cache[n]
            soln = set()
            for k in xrange(0, n - 2 + 1, 2):
                left = self.comb(k, cache)
                right = self.comb(n - 2 - k, cache)
                for sub1, sub2 in product(left, right):
                    soln.add('(' + sub1 + ')' + sub2)
                    soln.add(sub1 + '(' + sub2 + ')')
            cache[n] = soln
            return soln

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        cache = dict()
        return list(self.comb(2 * n, cache))