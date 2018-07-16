class Solution:
    def calcDepth(self, root, lev, depth):
        if root:
            lev = max(lev, \
                      self.calcDepth(root.left, lev + 1, depth), \
                      self.calcDepth(root.right, lev + 1, depth))
            depth[root] = lev
            return lev
        else:
            return 0

    def subtreeWithAllDeepest(self, root):
        depth = {None: 0}
        self.calcDepth(root, 0, depth)

        def rec(node):
            if node:
                if depth[node.left] > depth[node.right]:
                    return rec(node.left)
                elif depth[node.right] > depth[node.left]:
                    return rec(node.right)
                else:
                    return node

        return rec(root) 