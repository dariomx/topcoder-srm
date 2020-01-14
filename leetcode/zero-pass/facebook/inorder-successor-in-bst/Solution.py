class Solution(object):
    def inorderSuccessor(self, root, p):
        def rec(node, cand):
            if node is None:
                return cand
            elif node.val > p.val:
                return rec(node.left, node)
            else:
                return rec(node.right, cand)

        return rec(root, None)

