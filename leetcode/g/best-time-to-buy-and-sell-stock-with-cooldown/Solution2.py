class Solution(object):
    def profit(self, prices, start, end, cache):
        if (start, end) in cache:
            return cache[(start, end)]
        if start >= end:
            ret = 0
        else:
            max_prof = 0
            for i in xrange(start, end):
                for j in xrange(i + 1, end + 1):
                    diff = prices[j] - prices[i]
                    if diff > 0:
                        left = self.profit(prices, start, i - 2, cache)
                        right = self.profit(prices, j + 2, end, cache)
                        prof = diff + left + right
                        if prof > max_prof:
                            max_prof = prof
            ret = max_prof
        cache[(start, end)] = ret
        return ret

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        cache = dict()
        max_diff = 0
        min_i, max_i = -1, 0
        for i in xrange(n - 1):
            for j in xrange(i + 1, n):
                diff = prices[j] - prices[i]
                if diff > max_diff:
                    max_diff = diff
                    min_i, max_i = i, j
        if max_i < n:
            self.profit(prices, min_i, max_i, cache)
        return self.profit(prices, 0, len(prices) - 1, cache)
