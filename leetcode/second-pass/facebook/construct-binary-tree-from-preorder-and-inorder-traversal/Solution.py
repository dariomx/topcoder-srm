class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        io_idx = {x: i for (i, x) in enumerate(inorder)}

        def rec(sp, ep, si, ei):
            if sp > ep:
                return None
            else:
                x = preorder[sp]
                i = io_idx[x]
                n_left = i - si
                n_right = ei - i
                root = TreeNode(x)
                root.left = rec(sp + 1, sp + n_left, si, i - 1)
                root.right = rec(ep - n_right + 1, ep, i + 1, ei)
                return root

        n = len(io_idx)
        return rec(0, n - 1, 0, n - 1)
