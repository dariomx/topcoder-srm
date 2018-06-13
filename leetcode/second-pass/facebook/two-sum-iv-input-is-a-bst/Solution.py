class Solution:
    def findTarget(self, root, k):
        stack = [root]
        vals = dict()
        while stack:
            node = stack.pop()
            vals[node.val] = node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        for x in vals:
            if k - x in vals and vals[x] != vals[k - x]:
                return True
        return False