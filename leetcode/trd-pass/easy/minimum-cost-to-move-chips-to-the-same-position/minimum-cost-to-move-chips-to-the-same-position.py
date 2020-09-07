class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = [0, 0]
        for p in position:
            cnt[p % 2] += 1
        return min(cnt)

