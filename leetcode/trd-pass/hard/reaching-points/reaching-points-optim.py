# optim from phorum idea (integrate my initial conditions into the loop)

from collections import deque


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:
            return False
        elif sx == tx:
            return (ty - sy) % sx == 0
        elif sy == ty:
            return (tx - sx) % sy == 0
        queue = deque([(tx, ty)])
        while queue:
            x, y = queue.pop()
            if (x, y) == (sx, sy):
                return True
            elif x == sx and (sy - y) % x == 0:
                return True
            elif y == sy and (sx - x) % y == 0:
                return True
            for nx, ny in ((x - y, y), (x, y - x)):
                if nx < sx or ny < sy:
                    continue
                queue.append((nx, ny))
        return False

