class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        max_depth = 0
        stack = [(root, 0, root)]
        leaves = []
        parent = dict()
        while stack:
            node, depth, par = stack.pop()
            if node is None:
                continue
            parent[node] = par
            if depth == max_depth:
                leaves.append(node)
            elif depth > max_depth:
                max_depth = depth
                leaves = [node]
            for child in (node.left, node.right):
                stack.append((child, depth + 1, node))
        lca = set(leaves)
        while len(lca) > 1:
            lca = {parent[n] for n in lca}
        return lca.pop()
