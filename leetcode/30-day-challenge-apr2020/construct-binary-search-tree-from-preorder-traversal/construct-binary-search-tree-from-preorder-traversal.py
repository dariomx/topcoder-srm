class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            if node.val < stack[-1].val:
                stack[-1].left = node
            else:
                parent = stack[-1]
                while stack and node.val > stack[-1].val:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return root