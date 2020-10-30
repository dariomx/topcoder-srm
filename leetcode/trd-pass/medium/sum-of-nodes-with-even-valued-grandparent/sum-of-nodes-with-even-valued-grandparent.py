class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def rec(node, parent, grandPa):
            if node is None:
                return 0
            ret = 0
            if grandPa and grandPa.val % 2 == 0:
                ret += node.val
            for child in (node.left, node.right):
                ret += rec(child, node, parent)
            return ret

        return rec(root, None, None)

