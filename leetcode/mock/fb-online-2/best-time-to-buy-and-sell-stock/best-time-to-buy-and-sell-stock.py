class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_price = prices[0]
        profit = 0
        for price in prices[1:]:
            profit = max(profit, price - buy_price)
            buy_price = min(buy_price, price)
        return profit