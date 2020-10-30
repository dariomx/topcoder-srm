class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode,
                      target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while stack:
            srcNode, dstNode = stack.pop()
            if srcNode == target:
                return dstNode
            if srcNode.left:
                stack.append((srcNode.left, dstNode.left))
            if srcNode.right:
                stack.append((srcNode.right, dstNode.right))


