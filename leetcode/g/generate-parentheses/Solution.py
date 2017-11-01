class Solution(object):
    def calc_comb(self, n):
        if n == 0:
            return ['']
        else:
            comb = []
            for sub in self.calc_comb(n - 2):
                comb.append('()' + sub)
                comb.append('(' + sub + ')')
                comb.append(sub + '()')
            return comb

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(set(self.calc_comb(2 * n)))