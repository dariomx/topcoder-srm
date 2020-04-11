class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        buy = -prices[0]
        sell = 0
        for i in range(1, n):
            buy = max(buy, sell - prices[i])
            sell = max(sell, prices[i] + buy)
        return sell
