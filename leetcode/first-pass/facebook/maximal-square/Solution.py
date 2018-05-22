class Solution:
    def maximalSquare(self, matrix):
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        lines = dict()
        max_area = 0
        for i in range(n):
            for j in range(m):
                for k in range(j, m):
                    if matrix[i][k] == "0":
                        break
                    max_area = 1
                    key = (j, k)
                    if key in lines:
                        cnt, last_i, max_cnt = lines[key]
                        if i - 1 == last_i:
                            cnt += 1
                        else:
                            cnt = 1
                    else:
                        cnt = 1
                        max_cnt = cnt
                    lines[key] = cnt, i, max(max_cnt, cnt)
        for (i,j), (_, _, max_cnt) in lines.items():
            size = j - i + 1
            if max_cnt >= size:
                max_area = max(max_area, size**2)
        return max_area
