class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans += mat[i][i] + mat[n-1-i][i]
            if i == n-1-i:
                ans -= mat[i][i]
        return ans