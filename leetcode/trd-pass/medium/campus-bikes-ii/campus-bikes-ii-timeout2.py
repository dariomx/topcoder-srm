from itertools import combinations, permutations

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])
        def getBit(vec, i):
            return (vec & (1 << i)) >> i
        def setBit(vec, i, x):
            return (vec & ~(1 << i)) | (x << i)
        n, m = len(workers), len(bikes)
        ans = inf
        for comb in combinations(range(m), n):
            for perm in permutations(comb):
                cost = 0
                for i, j in enumerate(perm):
                    cost += dist(i, j)
                ans = min(ans, cost)
        return ans