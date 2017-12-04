"""
Here is one of the solutions found in literature:

0) Pick arbitrary starting node

1) Do a BFS/DFS search (it does not matter as trees have unique paths), keeping
   track of the farthest node (any will make the trick, as there could be
   several
   with same distance from starting node)

2) Repeat 1) but starting from the farthest node found. The path from this new
   starting point ands its new farthest node will be the diameter of the tree.

3) There is a theorem saying that center lies at the middle of the diameter,
   seen as a path. If such path has odd length, there are two centers.

"""
from collections import defaultdict


class Solution(object):
    def search_farthest(self, tree, start):
        stack = [(start, 0)]
        parent = dict()
        visited = set()
        max_dist = 0
        while stack:
            node, dist = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if dist > max_dist:
                max_dist = dist
                farthest = node
            for child in tree[node]:
                if child not in parent:
                    parent[child] = node
                stack.append((child, dist + 1))
        return max_dist, farthest, parent

    def findMinHeightTrees(self, n, edges):
        if not edges:
            return [0] * n
        tree = defaultdict(lambda: [])
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        start = tree.iterkeys().next()
        _, farthest1, _ = self.search_farthest(tree, start)
        max_dist, farthest2, parent = self.search_farthest(tree, farthest1)
        node = farthest2
        for _ in xrange(max_dist / 2):
            node = parent[node]
        roots = [node]
        if max_dist % 2 == 1:
            roots.append(parent[node])
        return roots
