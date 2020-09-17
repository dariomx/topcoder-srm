class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        rem = 0
        while numBottles > 0:
            ans += numBottles
            numBottles, rem = divmod(numBottles + rem, numExchange)
        return ans