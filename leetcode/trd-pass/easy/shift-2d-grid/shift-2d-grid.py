# wanted to do in place with cyclic-sort trick, but failed in life

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        size = n * m
        ans = [[0] * m for _ in range(n)]
        def get(i):
            x, y = divmod(i, m)
            return grid[x][y]
        def set(i, v):
            x, y = divmod(i, m)
            ans[x][y] = v
        for i in range(size):
            set((i + k) % size, get(i))
        return ans