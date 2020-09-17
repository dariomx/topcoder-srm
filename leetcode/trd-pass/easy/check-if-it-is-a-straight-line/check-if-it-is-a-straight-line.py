class Solution:
    def checkStraightLine(self, coord: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coord[0], coord[1]
        if x1 == x2:
            vert = True
        else:
            vert = False
            m = (y2 - y1) / (x2 - x1)
        if vert:
            for i in range(2, len(coord)):
                x, _ = coord[i]
                if x != x1:
                    return False
        else:
            for i in range(2, len(coord)):
                x, y = coord[i]
                if y - y1 != m*(x - x1):
                    return False
        return True