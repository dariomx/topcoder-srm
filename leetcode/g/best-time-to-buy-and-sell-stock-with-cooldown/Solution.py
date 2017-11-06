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
        cache = dict()
        return self.profit(prices, 0, len(prices) - 1, cache)
