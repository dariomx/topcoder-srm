WHITE = 1
GRAY = 2
BLACK = 3


class Solution:
    def buildGraph(self, edges):
        graph = defaultdict(list)
        nodes = set()
        in_deg = defaultdict(lambda: 0)
        for u, v in edges:
            graph[u].append(v)
            nodes.add(u)
            nodes.add(v)
            in_deg[v] += 1
        return graph, nodes, in_deg

    def findCycle(self, n, graph):
        def dfs(node, edges):
            nonlocal cycle
            if color[node] == BLACK:
                return
            elif color[node] == GRAY:
                for u, v in reversed(edges):
                    cycle.append((u, v))
                    if u == node:
                        break
            else:
                color[node] = GRAY
                for child in graph[node]:
                    dfs(child, edges + [(node, child)])
                color[node] = BLACK

        color = [WHITE] * (n + 1)
        cycle = []
        for start in range(1, n + 1):
            dfs(start, [])
        return cycle

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[
        int]:
        graph, nodes, in_deg = self.buildGraph(edges)
        if len(nodes) == len(in_deg):
            root = None
        else:
            root = (nodes - in_deg.keys()).pop()
        cycle = self.findCycle(len(nodes), graph)
        if cycle:
            edi = {tuple(e): i for (i, e) in enumerate(edges)}
            for u, v in sorted(cycle, key=edi.__getitem__, reverse=True):
                if root is None or in_deg[v] == 2:
                    return (u, v)
        else:  # there must be a node with two parents
            twopar = max(nodes, key=in_deg.__getitem__)
            for u, v in reversed(edges):
                if v == twopar:
                    return (u, v)
