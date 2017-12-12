def pprint2(min_x, max_x, min_y, max_y, rect):
    screen = [[0 for _ in xrange(min_x, max_x + 2)] for _ in
              xrange(min_y, max_y + 2)]
    print("%d %d" % (len(screen), len(screen[0])))
    rn = 1
    for x1, y1, x2, y2 in rect:
        print("rn = %d for %s" % (rn, str((x1, y1, x2, y2))))
        for x in xrange(x1 + 1, x2 + 1):
            for y in xrange(y1 + 1, y2 + 1):
                try:
                    if screen[y][x] == 0:
                        screen[y][x] += rn
                    else:
                        raise ValueError()
                except:
                    print("kk %d %d" % (x, y))
                    raise
        rn += 1
    to_char = lambda d: chr(ord('a') - 1 + d) if d > 0 else str(d)
    for row in screen:
        line = ''.join(map(to_char, row))
        print(line)


def pprint(min_x, max_x, min_y, max_y, grid):
    for y in xrange(min_y + 1, max_y + 1):
        line = ''
        for x in xrange(min_x + 1, max_x + 1):
            if (x, y) in grid:
                line += '*'
            else:
                line += '_'
        print(line)


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
        for x1, y1, x2, y2 in rect:
            for x in xrange(x1 + 1, x2 + 1):
                for y in xrange(y1 + 1, y2 + 1):
                    if (x, y) in grid:
                        return False
                    else:
                        grid.add((x, y))
        pprint2(min_x, max_x, min_y, max_y, rect)
        print("a ver %d == %d" % (len(grid), area))
        return len(grid) == area


rect = [[0, 0, 4, 1], [7, 0, 8, 2], [5, 1, 6, 4], [6, 0, 7, 2], [4, 0, 5, 1],
        [4, 2, 5, 3], [2, 1, 4, 3], [0, 2, 2, 3], [0, 1, 2, 2], [6, 2, 8, 3],
        [5, 0, 6, 1], [4, 1, 5, 2]]
print(Solution().isRectangleCover(rect))
