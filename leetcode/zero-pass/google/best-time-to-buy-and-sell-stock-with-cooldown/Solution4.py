class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        cache = dict()
        for i in xrange(n):
            cache[(i, i)] = 0
        for i in xrange(n - 1):
            j = i + 1
            if prices[i] < prices[j]:
                cache[(i, j)] = prices[j] - prices[i]
            else:
                cache[(i, j)] = 0
        # print(cache)
        for size in xrange(3, n + 1):
            for start in xrange(n - size + 1):
                end = start + size - 1
                cache[(start, end)] = max(0, prices[end] - prices[start])
                # print("start for %s with %s" % ((start,end), cache))
                for cut in xrange(start, end):
                    left = cache[(start, cut)]
                    if left == 0:
                        right = cache[(cut + 1, end)]
                    elif (cut + 2, end) in cache:
                        right = cache[(cut + 2, end)]
                    # print("exploring for %s with %d: %d %d" % \
                    #     ((start,end), cut, left, right))
                    cache[(start, end)] = max(cache[(start, end)], left + right)
                    # print("end for %s with %s" % ((start,end), cache))
        return cache[(0, n - 1)]
