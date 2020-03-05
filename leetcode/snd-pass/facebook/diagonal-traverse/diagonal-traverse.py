class Solution:
    #def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
    def findDiagonalOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        else:
            n = len(matrix[0])
        left_down = (+1, -1)
        right_up = (-1, +1)
        right = (0, +1)
        down = (+1, 0)
        next_pos = lambda p, sd: (p[0] + sd[0], p[1] + sd[1])
        valid_pos = lambda p: 0 <= p[0] < m and 0 <= p[1] < n
        trans = {left_down: (down, right), right_up: (right, down)}
        next_dir = {left_down: right_up, right_up: left_down}
        def take_pos(pos):
            nonlocal ans
            i, j = cpos
            ans.append(matrix[i][j])
        cdir = right_up
        cpos = 0, 0
        ans = []
        while cpos != (m-1, n-1):
            while True:
                take_pos(cpos)
                npos = next_pos(cpos, cdir)
                if valid_pos(npos):
                    cpos = npos
                else:
                    break
            for sdir in trans[cdir]:
                npos = next_pos(cpos, sdir)
                if valid_pos(npos):
                    cpos = npos
                    cdir = next_dir[cdir]
                    break
        take_pos(cpos)
        return ans

# main
m, n = 3000, 2000
matrix = [list(range(n)) for _ in range(m)]
Solution().findDiagonalOrder(matrix)