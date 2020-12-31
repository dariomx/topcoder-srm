from typing import List

from math import inf


class Solution:
    def minArea(self, image: List[List[str]], sx: int, sy: int) -> int:
        stack = [(sx, sy)]
        min_x, max_x = +inf, -inf
        min_y, max_y = +inf, -inf
        n, m = len(image), len(image[0])
        visited = set()
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
            for dx, dy in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m) or image[nx][ny] == '0':
                    continue
                stack.append((nx, ny))
        return (max_x - min_x + 1) * (max_y - min_y + 1)

