N = 1000000

class Solution:
    def getRect(self, points: Iterable[tuple[int, int]]) -> tuple[int, int, int, int]:
        min_x, max_x = inf, -inf
        min_y, max_y = inf, -inf
        for x, y in points:
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
        return min_x, max_x, min_y, max_y

    def neighbors(self, x, y, diag=False) -> Iterator[tuple[int, int]]:
        min_x, max_x, min_y, max_y = 0, N-1, 0, N-1
        deltas = ((-1, 0), (+1, 0), (0, +1), (0, -1))
        if diag:
            deltas += ((-1, -1), (-1, +1), (+1, -1), (+1, +1))
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            if min_x <= nx <= max_x and min_y <= ny <= max_y:
                yield nx, ny

    def getBlockedGraph(self, blocked: set[tuple[int, int]]) -> dict[int, set[tuple[int, int]]]:
        graph = defaultdict(set)
        for x, y in blocked:
            for nei in self.neighbors(x, y, diag=True):
                if nei not in blocked:
                    continue
                graph[x, y].add(nei)
                graph[nei].add((x, y))
        return graph

    def dfsComp(self, start: tuple[int, int],
                graph: dict[int, set[tuple[int, int]]]) -> set[int]:
        stack = [start]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            else:
                visited.add(node)
            for child in graph[node]:
                stack.append(child)
        return visited

    def getCC(self, graph: dict[int, set[tuple[int, int]]]) -> list[set[tuple[int, int]]]:
        visited = set()
        cc = []
        for node in graph:
            if node not in visited:
                comp = self.dfsComp(node, graph)
                cc.append(comp)
                visited |= comp
        return cc

    def isTrapped(self, p: tuple[int, int], comp: set[tuple[int, int]]) -> bool:
        stack = [p]
        visited = set()
        min_x, max_x, min_y, max_y = self.getRect(comp)
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            else:
                visited.add(node)
            x, y = node
            if not (min_x <= x <= max_x) or not (min_y <= y <= max_y):
                return False
            for child in self.neighbors(x, y):
                if child not in comp:
                    stack.append(child)
        return True

    def isReachable(self, source: tuple[int, int],
                    target: tuple[int, int], blocked: set[tuple[int, int]]) -> bool:
        queue = deque([source])
        visited = {source}
        min_x, max_x, min_y, max_y = self.getRect(blocked)
        while queue:
            node = queue.popleft()
            if node == target:
                return True
            x, y = node
            if not (min_x <= x <= max_x and min_y <= y <= max_y):
                break
            for child in self.neighbors(x, y):
                if child not in visited and child not in blocked:
                    visited.add(child)
                    queue.append(child)
        return False

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        source, target = tuple(source), tuple(target)
        blocked = {tuple(p) for p in blocked}
        graph = self.getBlockedGraph(blocked)
        for comp in self.getCC(graph):
            trap_src = self.isTrapped(source, comp)
            trap_tgt = self.isTrapped(target, comp)
            if trap_src and trap_tgt:
                return self.isReachable(source, target, comp)
            elif trap_src != trap_tgt:
                return False
        return True
