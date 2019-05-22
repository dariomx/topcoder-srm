class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        cache_depth = dict()

        def depth(node):
            if node in cache_depth:
                return cache_depth[node]
            if node is None:
                ret = 0
            else:
                ret = 1 + max(depth(node.left), depth(node.right))
            cache_depth[node] = ret
            return ret

        cache_diam = dict()

        def diam(node):
            if node in cache_diam:
                return cache_diam[node]
            if node is None:
                ret = depth
            else:
                left = diam(node.left)
                right = diam(node.right)
                ret = max(left, right, 1 + depth(left) + depth(right))
            cache_diam[node] = ret
            return ret

        return diam(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(root))