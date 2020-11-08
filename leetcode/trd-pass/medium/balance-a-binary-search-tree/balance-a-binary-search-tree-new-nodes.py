class Solution:
    def inorder(self, root, nodes):
        if root:
            self.inorder(root.left, nodes)
            nodes.append(root)
            self.inorder(root.right, nodes)

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

        nodes = list()
        self.inorder(root, nodes)
        return build(nodes, 0, len(nodes) - 1)
