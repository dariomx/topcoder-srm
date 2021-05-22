WHITE = 0
GRAY = 1
BLACK = 2

class Solution:
    def getMembers(self, m, group):
        members = defaultdict(set)
        for i, g in enumerate(group):
            if g < 0:
                g = m
                group[i] = g
                m += 1
            members[g].add(i)
        return members

    def buildGraphs(self, before, group):
        beforeG = defaultdict(set)
        groupG = defaultdict(set)
        for u, anc in enumerate(before):
            for v in anc:
                beforeG[v].add(u)
                gv, gu = group[v], group[u]
                if gv != gu:
                    groupG[gv].add(gu)
        return beforeG, groupG

    def dfs(self, node, graph, color, order, members):
        hasCycle = False
        if color[node] == GRAY:
            hasCycle = True
        elif color[node] == WHITE:
            color[node] = GRAY
            for child in (graph[node] & members):
                if self.dfs(child, graph, color, order, members):
                    hasCycle = True
                    break
            if not hasCycle:
                color[node] = BLACK
                order.appendleft(node)
        return hasCycle

    def topoSort(self, graph, color, nodes):
        hasCycle = False
        order = deque()
        for node in nodes:
            if color[node] == WHITE:
                if self.dfs(node, graph, color, order, nodes):
                    hasCycle = True
                    break
        return order, hasCycle

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        members = self.getMembers(m, group)
        beforeGraph, groupGraph = self.buildGraphs(beforeItems, group)
        beforeColor = [WHITE] * n
        _, cycleBefore = self.topoSort(beforeGraph, beforeColor, set(range(n)))
        if cycleBefore:
            return []
        groupColor = defaultdict(lambda: WHITE)
        groupOrder, groupCycle = self.topoSort(groupGraph, groupColor, members.keys())
        if groupCycle:
            return []
        ans = []
        beforeColor = [WHITE] * n
        topoGroup = lambda g: self.topoSort(beforeGraph, beforeColor, members[g])[0]
        return chain.from_iterable(map(topoGroup, groupOrder))
