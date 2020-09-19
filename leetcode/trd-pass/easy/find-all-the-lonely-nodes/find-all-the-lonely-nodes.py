class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        def rec(node):
            if node is None:
                return
            else:
                if node.left and not node.right:
                    ans.append(node.left.val)
                elif not node.left and node.right:
                    ans.append(node.right.val)
                rec(node.left)
                rec(node.right)

        # main
        ans = []
        rec(root)
        return ans
