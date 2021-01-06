class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def buy(i, tx):
            if i == n:
                if tx >= 0:
                    return 0
                else:
                    return -inf
            elif tx >= 0:
                return max(sell(i + 1, tx - 1) - prices[i], buy(i + 1, tx))
            else:
                return -inf

        @cache
        def sell(i, tx):
            if i == n:
                if tx >= 0:
                    return 0
                else:
                    return -inf
            elif tx >= 0:
                return max(buy(i + 1, tx) + prices[i], sell(i + 1, tx))
            else:
                return -inf

        return buy(0, k)
