# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, root):
        if root is None:
            return None
        stack = [root]
        nmap = dict()
        visited = set()
        while stack:
            old = stack.pop()
            if old in visited:
                continue
            visited.add(old)
            new = UndirectedGraphNode(old.label)
            nmap[old] = new
            for nei in old.neighbors:
                new.neighbors.append(nei)
                stack.append(nei)
        for new in nmap.values():
            new.neighbors = [nmap[nei] for nei in new.neighbors]
        return nmap[root]
