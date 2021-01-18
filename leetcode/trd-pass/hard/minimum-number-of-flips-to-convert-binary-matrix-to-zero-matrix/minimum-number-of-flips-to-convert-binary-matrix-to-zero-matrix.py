from copy import deepcopy


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        def flip(A, x, y):
            A[x][y] = 1 - A[x][y]
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < m and 0 <= ny < n:
                    A[nx][ny] = 1 - A[nx][ny]

        def encode(A):
            return sum(map(tuple, A), ())

        queue = deque()
        enc = encode(mat)
        if sum(enc) == 0:
            return 0
        else:
            queue.append((mat, 0))
            visited = {enc}
        while queue:
            node, dist = queue.popleft()
            for x in range(m):
                for y in range(n):
                    flip(node, x, y)
                    enc = encode(node)
                    if sum(enc) == 0:
                        return dist + 1
                    elif enc not in visited:
                        queue.append((deepcopy(node), dist + 1))
                        visited.add(enc)
                    flip(node, x, y)
        return -1
