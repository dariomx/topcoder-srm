class Solution:
    def isLineOverlap(self, s1, e1, s2, e2):
        s, e = min(s1, s2), max(e1, e2)
        return e - s < (e1 - s1) + (e2 - s2)

    def isRectangleOverlap(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return self.isLineOverlap(x1, x2, x3, x4) and \
               self.isLineOverlap(y1, y2, y3, y4)


