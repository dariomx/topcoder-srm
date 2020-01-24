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

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue
            if self.goodStart(i, gas, cost):
                return i
        return -1
