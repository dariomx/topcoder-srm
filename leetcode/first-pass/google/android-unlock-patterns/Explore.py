from collections import OrderedDict


class Solution:
    def __init__(self):
        N = (+1, 0)
        S = (-1, 0)
        E = (0, +1)
        W = (0, -1)
        NE = (-1, +1)
        NW = (-1, -1)
        SE = (+1, +1)
        SW = (+1, -1)
        self.dirs = [N, S, E, W, NE, NW, SE, SW]
        self.snei = dict()
        self.snei[(0, 0)] = [(1, 2), (2, 1)]
        self.snei[(0, 1)] = [(2, 0), (2, 2)]
        self.snei[(0, 2)] = [(1, 0), (2, 1)]
        self.snei[(1, 0)] = [(0, 2), (2, 2)]
        self.snei[(1, 1)] = []
        self.snei[(1, 2)] = [(0, 0), (2, 0)]
        self.snei[(2, 0)] = [(0, 1), (1, 2)]
        self.snei[(2, 1)] = [(0, 0), (0, 2)]
        self.snei[(2, 2)] = [(0, 1), (1, 0)]

    def neighbors(self, pos, visited):
        neis = self.snei[pos]
        for i, j in self.dirs:
            x, y = pos
            while True:
                x += i
                y += j
                if 0 <= x < 3 and 0 <= y < 3:
                    if (x, y) not in visited:
                        neis.append((x, y))
                        break
                else:
                    break
        return neis

    def dfs(self, pos, m, n, visited, soln):
        if pos in visited:
            return
        visited[pos] = True
        d = len(visited)
        if m <= d <= n:
            soln.add(tuple(visited.keys()))
        if d < n:
            for nei in self.neighbors(pos, visited):
                self.dfs(nei, m, n, visited, soln)
        del visited[pos]

    def numberOfPatterns(self, m, n):
        visited = OrderedDict()
        soln = set()
        for x in range(3):
            for y in range(3):
                visited.clear()
                self.dfs((x, y), m, n, visited, soln)
        return len(soln)

print(Solution().numberOfPatterns(1, 3))