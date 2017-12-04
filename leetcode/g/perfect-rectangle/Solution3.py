class Solution(object):
    def isRectangleCover(self, rect):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        min_x, min_y, _, _ = min(rect, key=lambda (x1, y1, x2, y2): (x1, y1))
        _, _, max_x, max_y = max(rect, key=lambda (x1, y1, x2, y2): (x2, y2))
        area = (max_x - min_x) * (max_y - min_y)
        grid = set()
        for y in xrange(min_y + 1, max_y + 1):
            grid.clear()
            for x1, y1, x2, y2 in rect:
                if y1 + 1 <= y <= y2:
                    for x in xrange(x1 + 1, x2 + 1):
                        if x in grid:
                            return False
                        else:
                            grid.add(x)
                            area -= 1
        return area == 0
