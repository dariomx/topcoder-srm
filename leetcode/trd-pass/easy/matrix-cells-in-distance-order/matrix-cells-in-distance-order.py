class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        cells = defaultdict(list)
        for i in range(R):
            for j in range(C):
                dist = abs(i - r0) + abs(j - c0)
                cells[dist].append((i, j))
        ans = []
        for dist in range(0, R+C+1):
            if dist in cells:
                ans += cells[dist]
        return ans