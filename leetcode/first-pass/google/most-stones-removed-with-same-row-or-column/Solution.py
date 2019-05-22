from collections import defaultdict


class Solution:
    def get_neighbors(self, stones):
        neiX = defaultdict(lambda: [])
        neiY = defaultdict(lambda: [])
        for x, y in stones:
            neiX[x].append((x, y))
            neiY[y].append((x, y))

        def neighbors(coord):
            x, y = coord
            yield from neiX[x]
            yield from neiY[y]

        return neighbors

    def dfs(self, start, visited, neighbors):
        cnt = 0
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            cnt += 1
            for nei in neighbors(node):
                stack.append(nei)
        return cnt - 1 if cnt > 0 else 0

    def removeStones(self, stones: 'List[List[int]]') -> 'int':
        ans = 0
        neighbors = self.get_neighbors(stones)
        visited = set()
        for x, y in stones:
            ans += self.dfs((x, y), visited, neighbors)
        return ans

