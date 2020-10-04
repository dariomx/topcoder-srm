WHITE = 0
GRAY  = 1
BLACK = 2

class Solution:
    def getRelation(self, seqs, refRel, n):
        rel = set()
        for seq in seqs:
            m = len(seq)
            for i in range(m):
                x = seq[i]
                if not (1 <= x <= n):  # note sure about this
                    return None
                for j in range(i + 1, m):
                    y = seq[j]
                    if x == y or \
                       (y, x) in rel or \
                       (refRel and (x, y) not in refRel):
                        return None
                    rel.add((x, y))
        return rel

    def dfs(self, graph, node, color, seq):
        if color[node] == BLACK:
            return
        elif color[node] == GRAY:
            raise ValueError("not a DAG!")
        color[node] = GRAY
        for nei in graph[node]:
            self.dfs(graph, nei, color, seq)
        color[node] = BLACK
        seq.appendleft(node)

    def topoSort(self, rel, n):
        graph = defaultdict(list)
        for x, y in rel:
            graph[x].append(y)
        color = {x:WHITE for x in range(1, n+1)}
        seq = deque()
        for node in range(1, n+1):
            if color[node] == WHITE:
                self.dfs(graph, node, color, seq)
        return list(seq)

    def sequenceReconstruction(self, org: List[int],
                               seqs: List[List[int]]) -> bool:
        n = len(org)
        refRel = self.getRelation([org], None, n)
        ltRel = self.getRelation(seqs, refRel, n)
        if len(seqs) == 0 or ltRel is None:
            return False
        elif len(ltRel) == 0:
            return len(org) <= 1
        else:
            return self.topoSort(ltRel, n) == org
