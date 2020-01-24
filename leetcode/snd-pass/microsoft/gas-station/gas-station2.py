class Solution:
    def goodStart(self, start, gas, cost):
        n = len(gas)
        tank = 0
        for i in range(start, start + n):
            j = i % n
            tank += gas[j] - cost[j]
            if tank < 0:
                return False
        return True

    def prefixDiff(self, gas, cost):
        n = len(gas)
        pdiff = [0] * n
        pdiff[n - 1] = gas[n - 1] - cost[n - 1]
        for i in range(n - 2, -1, -1):
            pdiff[i] = pdiff[i + 1] + gas[i] - cost[i]
        return pdiff

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pdiff = self.prefixDiff(gas, cost)
        for i in range(len(gas)):
            if pdiff[i] < 0:
                continue
            if self.goodStart(i, gas, cost):
                return i
        return -1
