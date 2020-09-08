class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        rmin = [-1] * n
        cmax = [-1] * m
        for i in range(n):
            for j in range(m):
                if rmin[i] < 0 or matrix[i][j] < matrix[i][rmin[i]]:
                    rmin[i] = j
                if cmax[j] < 0 or matrix[i][j] > matrix[cmax[j]][j]:
                    cmax[j] = i
        ans = []
        for i, j in enumerate(rmin):
            if i == cmax[j]:
                ans.append(matrix[i][j])
        return ans


