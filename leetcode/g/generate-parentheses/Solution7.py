from itertools import product


class Solution(object):
    def comb(self, n):
        if n == 0:
            return set([''])
        else:
            soln = set()
            for k in xrange(0, n - 2 + 1, 2):
                for sub1, sub2 in product(self.comb(k), self.comb(n - 2 - k)):
                    soln.add('(' + sub1 + ')' + sub2)
                    soln.add(sub1 + '(' + sub2 + ')')
            return soln

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(self.comb(2 * n))
