from collections import deque
from typing import List
from math import inf

class Solution:
    def neighbors(self, node):
        x, y = node
        for dx in (-1, 0, +1):
            for dy in (-1, 0, +1):
                if dx == 0 and dy == 0:
                    continue
                yield x + dx, y + dy

    def getRect(self, points):
        minX, maxX, minY, maxY = inf, -inf, inf, -inf
        for x, y in points:
            minX = min(minX, x)
            maxX = max(maxX, x)
            minY = min(minY, y)
            maxY = max(maxY, y)
        return minX, maxX, minY, maxY

    def inRect(self, p, rect):
        x, y = p
        minX, maxX, minY, maxY = rect
        return minX <= x <= maxX and minY <= y <= maxY

    def minDist(self, start, end, rect):
        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)
        while queue:
            node, dist = queue.popleft()
            print(len(visited), node, dist, rect)
            if node == end:
                return dist
            for child in self.neighbors(node):
                if child in visited or not self.inRect(child, rect):
                    continue
                visited.add(child)
                queue.append((child, dist + 1))
        raise ValueError("Could not reach " + end + " from " + start)

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        rect = self.getRect(points)
        for i in range(1, len(points)):
            p1, p2 = tuple(points[i - 1]), tuple(points[i])
            ans += self.minDist(p1, p2, rect)
        return ans

#main
points = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]
print(Solution().minTimeToVisitAllPoints(points))
