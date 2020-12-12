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
        @lru_cache
        def rec(i, used, avail, cost):
            nonlocal ans
            if i == n:
                ans = min(ans, cost)
            elif avail == 0 or avail < n - i or cost > ans:
                None
            else:
                for j in range(m):
                    if getBit(used, j) == 0:
                        used = setBit(used, j, 1)
                        rec(i + 1, used, avail - 1, cost + dist(i, j))
                        used = setBit(used, j, 0)
        rec(0, 0, m, 0)
        return ans