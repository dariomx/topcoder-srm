class Solution:
    def projectionArea(self, grid):
        xy, xz, yz = set(), set(), set()
        n, m = len(grid), len(grid[0])
        for x in range(n):
            for y in range(m):
                for z in range(grid[x][y]):
                    xy.add((x, y))
                    xz.add((x, z))
                    yz.add((y, z))
        return len(xy) + len(xz) + len(yz)
