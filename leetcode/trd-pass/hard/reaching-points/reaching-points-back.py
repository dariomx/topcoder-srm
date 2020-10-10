from collections import deque


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        queue = deque([(tx, ty)])
        while queue:
            x, y = queue.pop()
            if (x, y) == (sx, sy):
                return True
            for nx, ny in ((x - y, y), (x, y - x)):
                if nx < sx or ny < sy:
                    continue
                queue.append((nx, ny))
        return False

# main
print(Solution().reachingPoints(35, 13, 455955547, 420098884))
