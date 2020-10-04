# the trick about the symmetry is not mine

class Solution:
    def neighbors(self, ij):
        i, j = ij
        for d1 in (-2, 2):
            for d2 in (-1, +1):
                yield (i + d1, j + d2)
                yield (i + d2, j + d1)

    def constr(self, xy):
        x, y = xy
        return x >= -2 and y >= -2

    def minKnightMoves(self, x: int, y: int) -> int:
        start = (0, 0)
        end = (abs(x), abs(y))
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            node, depth = queue.popleft()
            if node == end:
                return depth
            for nei in self.neighbors(node):
                if nei in visited or not self.constr(nei):
                    continue
                visited.add(nei)
                queue.append((nei, depth + 1))

