class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        common = mat[0]
        for k in range(1, len(mat)):
            i = 0
            j = 0
            tmp = []
            while i < len(common) and j < len(mat[k]):
                if common[i] < mat[k][j]:
                    i += 1
                elif common[i] == mat[k][j]:
                    tmp.append(common[i])
                    i += 1
                    j += 1
                else:
                    j += 1
            if len(tmp) == 0:
                return -1
            else:
                common = tmp
        return common[0]
