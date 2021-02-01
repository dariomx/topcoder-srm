from itertools import chain

class Solution:
    def compress(self, arr):
        prev = None
        carr = []
        cnt = 0
        for x in chain(arr, [None]):
            if x == prev:
                cnt += 1
            else:
                if prev is not None:
                    carr += [prev] * min(2, cnt)
                prev = x
                cnt = 1
        return carr

    def buildGraph(self, arr):
        idx = defaultdict(list)
        for i, x in enumerate(arr):
            idx[x].append(i)
        graph = defaultdict(list)
        n = len(arr)
        for i, x in enumerate(arr):
            for j in chain(idx[x], (i-1, i+1)):
                if i != j and 0 <= j < n:
                    graph[i].append(j)
        return graph

    def minJumps(self, arr: List[int]) -> int:
        arr = self.compress(arr)
        graph = self.buildGraph(arr)
        queue = deque([(0, 0)])
        visited = {0}
        n = len(arr)
        while queue:
            node, steps = queue.popleft()
            if node == n-1:
                return steps
            for nei in graph[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                queue.append((nei, steps+1))
