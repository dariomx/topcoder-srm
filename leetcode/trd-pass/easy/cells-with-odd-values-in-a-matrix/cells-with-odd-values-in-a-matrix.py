class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rowCnt = [0] * n
        colCnt = [0] * m
        for i, j in indices:
            rowCnt[i] += 1
            colCnt[j] += 1
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += (rowCnt[i] + colCnt[j]) % 2
        return ans
