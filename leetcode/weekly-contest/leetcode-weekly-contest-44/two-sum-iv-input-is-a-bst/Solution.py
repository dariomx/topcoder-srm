# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_nodes(self, root):
        nodes = []
        stack = [root]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            nodes.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return nodes

    def search(self, root, node, k):
        if root is None or root == node:
            return False
        else:
            t = k - node.val
            if root.val == t:
                return True
            elif root.val < t:
                return self.search(root.right, node, k)
            else:
                return self.search(root.left, node, k)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        for node in self.get_nodes(root):
            if self.search(root, node, k):
                return True
        return False
