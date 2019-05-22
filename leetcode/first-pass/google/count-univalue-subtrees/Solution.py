class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def rec(node):
            if not node:
                return 0, 0
            elif not node.left and not node.right:
                return 1, 1
            elif not node.left and node.right:
                cntR, uniR = rec(node.right)
                uni = uniR
                if node.val == node.right.val and \
                                cntR == uniR:
                    uni += 1
                return 1 + cntR, uni
            elif node.left and not node.right:
                cntL, uniL = rec(node.left)
                uni = uniL
                if node.val == node.left.val and \
                                cntL == uniL:
                    uni += 1
                return 1 + cntL, uni
            else:
                cntL, uniL = rec(node.left)
                cntR, uniR = rec(node.right)
                uni = uniL + uniR
                if node.val == node.left.val and \
                                node.val == node.right.val and \
                                cntL == uniL and cntR == uniR:
                    uni += 1
                return 1 + cntL + cntR, uni

        _, uniCnt = rec(root)
        return uniCnt
    