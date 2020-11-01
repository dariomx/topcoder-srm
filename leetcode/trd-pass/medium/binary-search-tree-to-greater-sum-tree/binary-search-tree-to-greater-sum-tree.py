class Solution:
    def inorder(self, root, order):
        if root:
            self.inorder(root.left, order)
            order.append(root)
            self.inorder(root.right, order)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        inord = []
        self.inorder(root, inord)
        psum = 0
        for node in reversed(inord):
            tmp = node.val
            node.val += psum
            psum += tmp
        return root
