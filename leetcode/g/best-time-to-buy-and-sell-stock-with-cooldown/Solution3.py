class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        cache = dict()
        for i in xrange(n):
            cache[(i, i)] = 0
        for i in xrange(n - 1):
            j = i + 1
            if prices[i] < prices[j]:
                cache[(i, j)] = prices[j] - prices[i]
            else:
                cache[(i, j)] = 0
        print(cache)
        for size in xrange(3, n + 1):
            for start in xrange(n - size + 1):
                end = start + size - 1
                cache[(start, end)] = max(0, prices[end] - prices[start])
                # print("start for %s with %s" % ((start,end), cache))
                for cut in xrange(start, end):
                    if cut + 2 >= end:
                        continue
                    # print("exploring for %s with %d: %d" % ((start,end), cut,  cache[(start,cut)] + cache[(cut+1,end)]))
                    cache[(start, end)] = \
                        max(cache[(start, end)], \
                            cache[(start, cut)] + cache[(cut + 2, end)])
                    # print("end for %s with %s" % ((start,end), cache))
        return cache[(0, n - 1)]
