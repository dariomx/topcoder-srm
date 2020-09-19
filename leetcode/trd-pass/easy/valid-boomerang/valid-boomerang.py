class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        points = {tuple(p) for p in points}
        if len(points) < 3:
            return False
        x1, y1 = points.pop()
        x2, y2 = points.pop()
        if x1 == x2:
            vert = True
        else:
            vert = False
            m = (y2 - y1) / (x2 - x1)
        x, y = points.pop()
        if vert:
            return x != x1
        else:
            return y - y1 != m * (x - x1)


