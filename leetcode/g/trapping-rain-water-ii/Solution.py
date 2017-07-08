from sys import maxint


class Solution(object):
    def countValley(self, level, start, heightMap, visited):
        stack = [start]
        cnt = 0
        height = 1
        m, n = len(heightMap), len(heightMap[0])
        while stack:
            cell = stack.pop()
            if cell in visited:
                continue
            visited.add(cell)
            cnt += 1
            x, y = cell
            if x in (0, m - 1) or y in (0, n - 1):
                height = 0
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if not (0 <= i < m) or not (0 <= j < n):
                    continue
                if heightMap[i][j] < level:
                    stack.append((i, j))
        return cnt * height

    def countLevel(self, level, heightMap):
        cnt = 0
        visited = set()
        m, n = len(heightMap), len(heightMap[0])
        for x in xrange(m):
            for y in xrange(n):
                if heightMap[x][y] < level:
                    cnt += self.countValley(level, (x, y), \
                                            heightMap, visited)
        return cnt

    def getMinMax(self, heightMap):
        hmin, hmax = maxint, 0
        m, n = len(heightMap), len(heightMap[0])
        for x in xrange(m):
            for y in xrange(n):
                hmin = min(hmin, heightMap[x][y])
                hmax = max(hmax, heightMap[x][y])
        return hmin, hmax

    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) == 0 or len(heightMap[0]) == 0:
            return 0
        cnt = 0
        hmin, hmax = self.getMinMax(heightMap)
        for level in xrange(hmin + 1, hmax + 1):
            cnt += self.countLevel(level, heightMap)
        return cnt

heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
heightMap = []
heightMap = [[19383,10886,12777,16915,17793,18335,15386,10492,16649,11421],[12362,27,8690,59,7763,3926,540,3426,9172,5736],[15211,5368,2567,6429,5782,1530,2862,5123,4067,3135],[13929,9802,4022,3058,3069,8167,1393,8456,5011,8042],[16229,7373,4421,4919,3784,8537,5198,4324,8315,4370],[16413,3526,6091,8980,9956,1873,6862,9170,6996,7281],[12305,925,7084,6327,336,6505,846,1729,1313,5857],[16124,3895,9582,545,8814,3367,5434,364,4043,3750],[11087,6808,7276,7178,5788,3584,5403,2651,2754,2399],[19932,5060,9676,3368,7739,12,6226,8586,8094,7539]]
print(Solution().trapRainWater(heightMap))