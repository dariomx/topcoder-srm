class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        hor_diag = ((i, 0) for i in range(m))
        ver_diag = ((0, j) for j in range(1, n))
        for si, sj in chain(hor_diag, ver_diag):
            i, j = si, sj
            cnt = [0] * 101
            while i < m and j < n:
                cnt[mat[i][j]] += 1
                i, j = i + 1, j + 1
            i, j = si, sj
            x = 1
            while i < m and j < n:
                while cnt[x] == 0:
                    x += 1
                mat[i][j] = x
                cnt[x] -= 1
                i, j = i + 1, j + 1
        return mat
