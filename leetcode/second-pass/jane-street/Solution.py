class Solution:
    def robotSim(self, commands, obstacles):
        def mult(A, v):
            x, y = v
            v[0] = A[0][0] * x + A[0][1] * y
            v[1] = A[1][0] * x + A[1][1] * y

        obstacles = {(x, y) for (x, y) in obstacles}
        L90 = [[0, -1], [1, 0]]
        R90 = [[0, 1], [-1, 0]]
        rot = {-2: L90, -1: R90}
        dir = [0, 1]
        pos = [0, 0]
        ans = 0
        for cmd in commands:
            if cmd < 0:
                mult(rot[cmd], dir)
            else:
                dx, dy = dir
                for _ in range(cmd):
                    if (pos[0] + dx, pos[1] + dy) in obstacles:
                        break
                    pos[0] += dx
                    pos[1] += dy
            ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
        return ans
