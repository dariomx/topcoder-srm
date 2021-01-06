class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        buy = [[0] * (k + 1) for _ in range(n + 1)]
        sell = [[0] * (k + 1) for _ in range(n + 1)]
        for j in range(1, k + 1):
            buy[n][j] = -inf
            sell[n][j] = -inf
        for i in range(n):
            for k in range(1, k + 1):
                buy[i][k] = max(sell[i - 1][k - 1] - prices[i], buy[i - 1][k])
                sell[i][k] = max(buy[i - 1][k] + prices[i], sell[i - 1][k])
        return max(sell[n - 1])
