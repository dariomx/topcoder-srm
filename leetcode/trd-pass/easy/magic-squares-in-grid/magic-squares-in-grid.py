# not very proud of this, really, but question was kinda ugly

class Solution:
    def sumRowCol(self, grid, i, j, inc_i, inc_j, vals, size=3, min_val=1,
                  max_val=9):
        s = 0
        for k in range(size):
            v = grid[i][j]
            if not (min_val <= v <= max_val):
                return -1
            s += v
            vals.add(v)
            i += inc_i
            j += inc_j
        return s

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        vals = set()
        for i in range(n - 2):
            for j in range(m - 2):
                vals.clear()
                r0 = self.sumRowCol(grid, i, j, 0, 1, vals)
                if len(vals) != 3:
                    continue
                r1 = self.sumRowCol(grid, i + 1, j, 0, 1, vals)
                if r1 != r0 or len(vals) != 6:
                    continue
                r2 = self.sumRowCol(grid, i + 2, j, 0, 1, vals)
                if r2 != r1 or len(vals) != 9:
                    continue
                c0 = self.sumRowCol(grid, i, j, 1, 0, vals)
                if c0 != r2:
                    continue
                c1 = self.sumRowCol(grid, i, j + 1, 1, 0, vals)
                if c1 != c0:
                    continue
                c2 = self.sumRowCol(grid, i, j + 2, 1, 0, vals)
                if c2 != c1:
                    continue
                d1 = grid[i + 0][j + 0] + grid[i + 1][j + 1] + grid[i + 2][
                    j + 2]
                if d1 != c2:
                    continue
                d2 = grid[i + 0][j + 2] + grid[i + 1][j + 1] + grid[i + 2][
                    j + 0]
                if d2 != d1:
                    continue
                ans += 1
        return ans
