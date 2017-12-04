from itertools import product


class Solution(object):
    def comb(self, n):
        if n == 0:
            return ['']
        else:
            ret = []
            for k in xrange(0, n - 2 + 1, 2):
                for sub1, sub2 in product(self.comb(k), self.comb(n - 2 - k)):
                    ret.append('(' + sub1 + ')' + sub2)
                    ret.append(sub1 + '(' + sub2 + ')')
            return ret

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(set(self.comb(2 * n)))
