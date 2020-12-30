class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        graph = defaultdict(list)
        for bus, stops in enumerate(routes):
            u = -(bus + 1)
            for v in stops:
                graph[u].append(v)
                graph[v].append(u)
        queue = deque([(S, 0)])
        visited = set([S])
        while queue:
            node, cnt = queue.popleft()
            if node == T:
                return cnt
            elif node < 0:
                cnt += 1
            for child in graph[node]:
                if child in visited:
                    continue
                visited.add(child)
                queue.append((child, cnt))
        return -1