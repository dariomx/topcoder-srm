from math import inf


class Solution:
    def coinChange(self, coins, amount):
        rec = [inf] * (amount + 1)
        rec[0] = 0
        for c in coins:
            if c <= amount:
                rec[c] = 1
        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    rec[x] = min(rec[x], rec[x - c] + 1)
        return rec[amount] if rec[amount] < inf else -1

