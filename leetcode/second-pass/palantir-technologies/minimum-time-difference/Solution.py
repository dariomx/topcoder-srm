from math import inf

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        bitmap = [None for _ in range(24)]
        rangem = [None for _ in range(24)]
        for ts in timePoints:
            h, m = map(int, ts.split(':'))
            if not bitmap[h]:
                bitmap[h] = [False] * 60
                rangem[h] = [inf, -inf]
            if bitmap[h][m]:
                return 0
            bitmap[h][m] = True
            rangem[h][0] = min(rangem[h][0], m)
            rangem[h][1] = max(rangem[h][1], m)
        ans, prev, min_i, max_i = inf, inf, inf, -inf
        for h in range(24):
            if not bitmap[h]:
                continue
            for m in range(rangem[h][0], rangem[h][1]+1):
                if not bitmap[h][m]:
                    continue
                i = h*60 + m
                min_i, max_i = min(min_i, i), max(max_i, i)
                ans = min(ans, abs(prev - i))
                prev = i
        return min(ans, 1440 - abs(min_i - max_i))