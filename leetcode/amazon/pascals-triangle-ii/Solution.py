"""
Python3 solution with O(k) time and space

The trick is to pre-compute all the factorials we will need, and that
can be done in linear time by reusing the previously computed value.
"""

class Solution:
    def getRow(self, k):
        fact = dict()
        fact[0] = 1
        for i in range(1, k + 1):
            fact[i] = fact[i - 1] * i

        def comb(n, m):
            return int(fact[n] / (fact[n - m] * fact[m]))

        return [comb(k, i) for i in range(k + 1)]
