from collections import deque


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        rect = deque(sorted(rectangles))
        min_x, min_y = rect[0][0], rect[0][1]
        _, _, max_x, max_y = max(rect, key=lambda (x1, y1, x2, y2): (x2, y2))
        area = (max_x - min_x) * (max_y - min_y)
        corner = set()
        corner.add((rect[0][0], rect[0][1]))
        while area > 0 and rect:
            x1, y1, x2, y2 = rect.popleft()
            if (x1, y1) in corner:
                area -= (x2 - x1) * (y2 - y1)
                corner.remove((x1, y1))
                corner.add((x1, y2))
                corner.add((x2, y1))
            else:
                print("could not allocate %s" % str((x1, y1, x2, y2)))
                break
        print("area = %d, rect = %s" % (area, str(rect)))
        return area == 0 and not rect


