class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        best_upto = [0] * n
        pmin = prices[0]
        for i in range(1, n):
            best_upto[i] = max(best_upto[i-1], prices[i] - pmin)
            pmin = min(pmin, prices[i])
        best_from = 0
        pmax = prices[n-1]
        best_split = 0
        for i in reversed(range(1, n-1)):
            best_from = max(best_from, pmax - prices[i])
            pmax = max(pmax, prices[i])
            best_split = max(best_split, best_upto[i-1] + best_from)
        return max(best_split, best_upto[n-1], best_from)
