class Solution:
    def average(self, salary: List[int]) -> float:
        minS, maxS, sumS = inf, -inf, 0
        for x in salary:
            minS = min(minS, x)
            maxS = max(maxS, x)
            sumS += x
        return (sumS - minS - maxS) / (len(salary) - 2)
