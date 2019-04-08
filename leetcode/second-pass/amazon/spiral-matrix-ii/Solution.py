RIGHT = (0, +1)
LEFT = (0, -1)
DOWN = (+1, 0)
UP = (-1, 0)


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        trans = {RIGHT: DOWN, DOWN: LEFT, LEFT: UP, UP: RIGHT}
        x, y, cnt = 0, 0, 1
        sx, sy, k = 0, 0, n
        dir = RIGHT
        while cnt <= n * n:
            ans[x][y] = cnt
            cnt += 1
            nx, ny = x + dir[0], y + dir[1]
            if not (sx <= nx < sx + k and sy <= ny < sy + k):
                dir = trans[dir]
                x, y = x + dir[0], y + dir[1]
            elif (nx, ny) == (sx, sy):
                sx, sy, k = sx + 1, sy + 1, k - 2
                x, y = sx, sy
            else:
                x, y = nx, ny
        return ans


