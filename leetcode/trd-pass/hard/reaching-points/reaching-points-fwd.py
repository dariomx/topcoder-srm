from collections import deque


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        queue = deque([(sx, sy)])
        i = 0
        while queue:
            x, y = queue.pop()
            if i % 100000 == 0:
                print(x, y)
            i += 1
            if (x, y) == (tx, ty):
                return True
            for nx, ny in ((x + y, y), (x, x + y)):
                if nx > tx or ny > ty:
                    continue
                queue.append((nx, ny))
        return False

# main
print(Solution().reachingPoints(35, 13, 455955547, 420098884))
