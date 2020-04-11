class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        sell[0] = 0
        for i in range(1, n):
            buy[i] = max((sell[j] - prices[i] for j in range(i)))
            sell[i] = max((prices[i] + buy[j] for j in range(i)))
        return max(sell)
