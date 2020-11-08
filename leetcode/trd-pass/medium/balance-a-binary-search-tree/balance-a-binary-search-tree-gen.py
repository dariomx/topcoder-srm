class Solution:
    def inorder(self, root):
        if root:
            yield from self.inorder(root.left)
            yield root
            yield from self.inorder(root.right)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        def build(nodes, i, j):
            if i > j:
                return None
            else:
                half = (i + j) // 2
                root = TreeNode(nodes[half].val)
                root.left = build(nodes, i, half - 1)
                root.right = build(nodes, half + 1, j)
                return root

        nodes = list(self.inorder(root))
        return build(nodes, 0, len(nodes) - 1)
