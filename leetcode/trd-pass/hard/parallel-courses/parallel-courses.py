class Solution:
    def getGraphDep(self, N, relations):
        graph = defaultdict(list)
        dep = [0] * (N + 1)
        for x, y in relations:
            graph[x].append(y)
            dep[y] += 1
        return graph, dep

    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph, dep = self.getGraphDep(N, relations)
        queue = deque(((x, 0) for x in range(1, N + 1) if dep[x] == 0))
        prevLev = None
        sem, courses = 0, 0
        while queue:
            x, lev = queue.popleft()
            courses += 1
            if lev != prevLev:
                sem += 1
                prevLev = lev
            for y in graph[x]:
                dep[y] -= 1
                if dep[y] == 0:
                    queue.append((y, lev + 1))
        if courses == N:
            return sem
        else:
            return -1
