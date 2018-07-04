class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0
        prev_open, prev_closed = -prices[0], 0
        for i in range(1, n):
            curr_open = max(prev_open, prev_closed - prices[i])
            curr_closed = max(prev_closed, prev_open + prices[i] - fee)
            prev_open, prev_closed = curr_open, curr_closed
        return max(prev_open, prev_closed)




